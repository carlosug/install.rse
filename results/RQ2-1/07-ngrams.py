import json
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import seaborn as sns
import pandas as pd
from wordcloud import WordCloud
from scipy.stats import ttest_ind

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Load the JSON file
output = "extractor/02_combined_installation_readmes.json"

# Load the JSON file
with open(output, 'r') as file:
    data = json.load(file)

# Initialize counters and trackers for years
year_stats = defaultdict(lambda: {
    'total_count': 0,
    'with_instructions': 0,
    'without_instructions': 0,
    'total_unique_results': 0,
    'min_results': float('inf'),
    'max_results': float('-inf'),
    'repo_count': 0,
    'language_stats': defaultdict(int),  # Nested dictionary for language stats per year
    'total_tokens': 0,  # Total tokens for unique results
    'bi_gram_counter': Counter(),  # Counter for bi-grams
    'tri_gram_counter': Counter()  # Counter for tri-grams
})

# Initialize a set to store unique programming languages
unique_languages = set()
language_counts = defaultdict(int)

# Function to sanitize text
def sanitize_text(text):
    if not text or not isinstance(text, str):
        return ""
    sanitized = text.replace('!', '`!')  # Customize the regex to include any specific characters you'd like to remove
    sanitized = sanitized.lower()
    return sanitized

# Updated function to extract n-grams
def extract_ngrams(text, num):
    sanitized_text = sanitize_text(text)  # Sanitize the text before processing
    if not sanitized_text:
        return []
    try:
        tokens = word_tokenize(sanitized_text)
        tokens = [token for token in tokens if token.isalnum()]  # Remove any remaining non-alphanumeric tokens
        n_grams = ngrams(tokens, num)
        return [' '.join(grams) for grams in n_grams]
    except Exception as e:
        print(f"Error tokenizing text: {text}\nException: {e}")
        return []

# Loop through each entry in the JSON data
for repo_id, repo in data.items():
    date_created = repo.get('date_created', None)
    
    # Check if date_created is a list and extract the year
    if isinstance(date_created, list) and len(date_created) > 0:
        date_info = date_created[0].get('result', {}).get('value', None)
        if date_info:
            year = date_info.split('-')[0]  # Extract the year
        else:
            year = 'unknown'
    else:
        year = 'unknown'
    
    # Update total count for the year
    year_stats[year]['total_count'] += 1
    
    # Check for installation instructions
    installation_instructions = repo.get('installation_instructions', [])
    if isinstance(installation_instructions, str) and installation_instructions == "No installation instructions found.":
        num_results = 0
    else:
        num_results = len(installation_instructions)
    
    if num_results > 0:
        year_stats[year]['with_instructions'] += 1
    else:
        year_stats[year]['without_instructions'] += 1
    
    # Update stats for the year
    year_stats[year]['total_unique_results'] += num_results
    year_stats[year]['min_results'] = min(year_stats[year]['min_results'], num_results)
    year_stats[year]['max_results'] = max(year_stats[year]['max_results'], num_results)
    year_stats[year]['repo_count'] += 1

    # Calculate total tokens for unique results
    for instruction in installation_instructions:
        if isinstance(instruction, dict):
            instruction_text = instruction.get('result', {}).get('value', "")
            if not isinstance(instruction_text, str):  # Ensure it's a string
                instruction_text = ""
        elif isinstance(instruction, str):
            instruction_text = instruction
        else:
            instruction_text = ""  # Handle unexpected types
        
        tokens = len(instruction_text.split())
        year_stats[year]['total_tokens'] += tokens

        # Extract bi-grams and tri-grams
        bi_grams = extract_ngrams(instruction_text, 2)
        tri_grams = extract_ngrams(instruction_text, 3)
        year_stats[year]['bi_gram_counter'].update(bi_grams)
        year_stats[year]['tri_gram_counter'].update(tri_grams)

    # Check for programming languages
    programming_languages = repo.get('programming_languages', "No programming languages found.")
    
    # Handle different types of programming_languages
    if isinstance(programming_languages, list):
        if not programming_languages:
            year_stats[year]['language_stats']["No programming languages found."] += 1
        else:
            for language in programming_languages:
                if isinstance(language, dict):
                    language_value = language.get('result', {}).get('value', "Unknown language (dict)")
                    year_stats[year]['language_stats'][language_value] += 1
                    unique_languages.add(language_value)
                    language_counts[language_value] += 1
                else:
                    year_stats[year]['language_stats'][language] += 1
                    unique_languages.add(language)
                    language_counts[language] += 1
    elif isinstance(programming_languages, str):
        year_stats[year]['language_stats'][programming_languages] += 1
        unique_languages.add(programming_languages)
        language_counts[programming_languages] += 1
    elif isinstance(programming_languages, dict):
        language_value = programming_languages.get('result', {}).get('value', "Unknown language (dict)")
        year_stats[year]['language_stats'][language_value] += 1
        unique_languages.add(language_value)
        language_counts[language_value] += 1

# Function to prepare data for plotting
def prepare_ngram_data(year_stats, ngram_type='bi_gram', top_n=3):
    data = []
    years = sorted(year_stats.keys())

    for year in years:
        stats = year_stats[year]
        if ngram_type == 'bi_gram':
            ngram_counter = stats['bi_gram_counter']
        elif ngram_type == 'tri_gram':
            ngram_counter = stats['tri_gram_counter']
        else:
            raise ValueError("ngram_type must be 'bi_gram' or 'tri_gram'")

        most_common_ngrams = ngram_counter.most_common(top_n)
        for ngram, count in most_common_ngrams:
            data.append({'Year': year, 'N-gram': ngram, 'Count': count})

    return pd.DataFrame(data)

def plot_ngrams_multigrid(year_stats, ngram_type='bi_gram', top_n=3):
    data = prepare_ngram_data(year_stats, ngram_type, top_n)
    
    # Perform t-tests and annotate p-values
    years = data['Year'].unique()
    p_values = {}
    
    for i in range(len(years)):
        for j in range(i + 1, len(years)):
            year1 = years[i]
            year2 = years[j]
            data1 = data[data['Year'] == year1]['Count']
            data2 = data[data['Year'] == year2]['Count']
            t_stat, p_val = ttest_ind(data1, data2, equal_var=False)
            p_values[(year1, year2)] = p_val

    g = sns.FacetGrid(data, col="Year", col_wrap=4, height=4, sharex=False, sharey=False)
    g.map_dataframe(sns.boxplot, x="N-gram", y="Count", palette="pastel", legend=False)
    g.set_axis_labels("N-gram", "Count")
    g.set_titles(col_template="{col_name}")

    # Annotate p-values
    for ax, col_name in zip(g.axes.flat, g.col_names):
        year = col_name
        for (year1, year2), p_val in p_values.items():
            if year == year1 or year == year2:
                ax.annotate(f'p-value ({year1} vs {year2}): {p_val:.2e}', xy=(0.5, 0.95), xycoords='axes fraction', ha='center', va='top', fontsize=10, color='red')

    plt.tight_layout()
    plt.show()

# Function to plot scatter plot of top 5 n-grams vs year_stats
def plot_ngrams_scatter(year_stats, ngram_type='bi_gram', top_n=5):
    data = prepare_ngram_data(year_stats, ngram_type, top_n)
    
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=data, x="Year", y="Count", hue="N-gram", style="N-gram", palette="deep", s=100)
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.title(f"Top {top_n} {ngram_type.replace('_', ' ')}s by Year")
    plt.legend(title="N-gram")
    plt.tight_layout()
    plt.show()

# Example usage
plot_ngrams_scatter(year_stats, ngram_type='bi_gram', top_n=5)

# Alternative visualization techniques

# Bar Plot
def plot_ngrams_bar(year_stats, ngram_type='bi_gram', top_n=3):
    data = prepare_ngram_data(year_stats, ngram_type, top_n)
    plt.figure(figsize=(12, 8))
    sns.barplot(data=data, x="Count", y="N-gram", hue="Year", palette="pastel")
    plt.xlabel("Count")
    plt.ylabel("N-grams")
    plt.title(f"Top {top_n} {ngram_type.replace('_', ' ')}s by Year")
    plt.legend(title="Year")
    plt.tight_layout()
    plt.show()

# Heatmap
def plot_ngrams_heatmap(year_stats, ngram_type='bi_gram', top_n=3):
    data = prepare_ngram_data(year_stats, ngram_type, top_n)
    pivot_table = data.pivot_table(index="N-gram", columns="Year", values="Count", fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
    plt.xlabel("Year")
    plt.ylabel("N-grams")
    plt.title(f"Heatmap of Top {top_n} {ngram_type.replace('_', ' ')}s by Year")
    plt.tight_layout()
    plt.show()

# Word Cloud
def plot_ngrams_wordcloud(year_stats, ngram_type='bi_gram', top_n=3):
    data = prepare_ngram_data(year_stats, ngram_type, top_n)
    ngram_counts = data.groupby('N-gram')['Count'].sum().to_dict()
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(ngram_counts)
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud of Top {top_n} {ngram_type.replace('_', ' ')}s")
    plt.show()

# Example usage
plot_ngrams_multigrid(year_stats, ngram_type='bi_gram', top_n=3)
plot_ngrams_multigrid(year_stats, ngram_type='tri_gram', top_n=3)
plot_ngrams_bar(year_stats, ngram_type='bi_gram', top_n=3)
plot_ngrams_bar(year_stats, ngram_type='tri_gram', top_n=3)
plot_ngrams_heatmap(year_stats, ngram_type='bi_gram', top_n=3)
plot_ngrams_heatmap(year_stats, ngram_type='tri_gram', top_n=3)
plot_ngrams_wordcloud(year_stats, ngram_type='bi_gram', top_n=3)
plot_ngrams_wordcloud(year_stats, ngram_type='tri_gram', top_n=3)