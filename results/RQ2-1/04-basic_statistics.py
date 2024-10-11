import json
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Last output for analysis:
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
    'total_tokens': 0  # Total tokens for unique results
})

# Initialize a set to store unique programming languages
unique_languages = set()
language_counts = defaultdict(int)

# List to store repositories with "Unknown language (dict)"
unknown_language_repos = []

# List to store languages found in 'Others'
others_languages = []

def sanitize_text(text):
    if not text or not isinstance(text, str):
        return ""

    # Remove problematic characters, such as punctuation and symbols
    sanitized = re.sub(r'[^\w\s]', '', text)  # Keeps only alphanumeric characters and spaces

    # Optionally, you can also convert the text to lowercase to normalize it
    sanitized = sanitized.lower()

    return sanitized

def extract_ngrams(text, num):
    sanitized_text = sanitize_text(text)  # Sanitize the text before processing
    if not sanitized_text:
        return []

    try:
        tokens = word_tokenize(sanitized_text)
    except Exception as e:
        print(f"Error tokenizing text: {sanitized_text}")
        print(f"Exception: {e}")
        return []

    tokens = [token for token in tokens if token.isalnum()]  # Remove any remaining non-alphanumeric tokens
    n_grams = ngrams(tokens, num)
    return [' '.join(grams) for grams in n_grams]

# Initialize a counter for n-grams
bi_gram_counter = Counter()
tri_gram_counter = Counter()

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
            if instruction_text:  # Ensure instruction_text is not empty
                tokens = len(instruction_text.split())
                year_stats[year]['total_tokens'] += tokens

                # Extract bi-grams and tri-grams
                bi_grams = extract_ngrams(instruction_text, 2)
                tri_grams = extract_ngrams(instruction_text, 3)
                bi_gram_counter.update(bi_grams)
                tri_gram_counter.update(tri_grams)

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
                    if language_value == "Unknown language (dict)":
                        unknown_language_repos.append(repo_id)
                else:
                    year_stats[year]['language_stats'][language] += 1
                    unique_languages.add(language)
                    language_counts[language] += 1
    elif isinstance(programming_languages, str):
        year_stats[year]['language_stats'][programming_languages] += 1
        unique_languages.add(programming_languages)
        language_counts[programming_languages] += 1
        if programming_languages == "Unknown language (dict)":
            unknown_language_repos.append(repo_id)
    elif isinstance(programming_languages, dict):
        language_value = programming_languages.get('result', {}).get('value', "Unknown language (dict)")
        year_stats[year]['language_stats'][language_value] += 1
        unique_languages.add(language_value)
        language_counts[language_value] += 1
        if language_value == "Unknown language (dict)":
            unknown_language_repos.append(repo_id)

# Print the table sorted by year in descending order
print(f"{'Year':<10} {'Total Count':<15} {'With Instructions':<20} {'Without Instructions':<20} {'Total Unique Results':<20} {'Min Results':<15} {'Max Results':<15} {'Repo Count':<15}")
for year in sorted(year_stats.keys(), reverse=True):
    stats = year_stats[year]
    print(f"{year:<10} {stats['total_count']:<15} {stats['with_instructions']:<20} {stats['without_instructions']:<20} {stats['total_unique_results']:<20} {stats['min_results']:<15} {stats['max_results']:<15} {stats['repo_count']:<15}")

# Prepare data for plotting
years = sorted(year_stats.keys())
num_years = len(years)
cols = 6  # Number of columns in the grid
rows = (num_years + cols - 1) // cols  # Calculate the number of rows needed

fig, axes = plt.subplots(rows, cols, figsize=(25, 5 * rows))
axes = axes.flatten()  # Flatten the 2D array of axes

for i, year in enumerate(years):
    stats = year_stats[year]
    languages = list(stats['language_stats'].keys())
    counts = list(stats['language_stats'].values())
    
    # Group the programming languages
    grouped_counts = {
        'Python': 0,
        'C++': 0,
        'Java': 0,
        'Others': 0
    }

    for language, count in zip(languages, counts):
        if language.lower() == 'python':
            grouped_counts['Python'] += count
        elif language.lower() == 'c++':
            grouped_counts['C++'] += count
        elif language.lower() == 'java':
            grouped_counts['Java'] += count
        else:
            grouped_counts['Others'] += count
            others_languages.append(language)  # Collect languages in 'Others'

    grouped_languages = list(grouped_counts.keys())
    grouped_counts_values = list(grouped_counts.values())

    axes[i].bar(grouped_languages, grouped_counts_values, color='skyblue')
    axes[i].set_xlabel('Programming Languages', fontsize=8)
    axes[i].set_ylabel('Count', fontsize=8)
    axes[i].set_title(f'Year: {year}', fontsize=10)
    axes[i].tick_params(axis='x', rotation=45, labelsize=8)

# Remove any unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()

# Calculate average number of tokens per unique result per year
average_tokens_per_year = {}
for year, stats in year_stats.items():
    if stats['total_unique_results'] > 0:
        average_tokens_per_year[year] = stats['total_tokens'] / stats['total_unique_results']
    else:
        average_tokens_per_year[year] = 0

# Plot the time series graph
years = sorted(average_tokens_per_year.keys())
average_tokens = [average_tokens_per_year[year] for year in years]

plt.figure(figsize=(10, 5))
plt.plot(years, average_tokens, marker='o', linestyle='-', color='b')
plt.xlabel('Year')
plt.ylabel('Average Number of Tokens per Unique Result')
plt.title('Average Number of Tokens per Unique Result per Year')
plt.grid(True)
plt.show()

# Print the number of distinct programming languages
print(f"Number of distinct programming languages: {len(unique_languages)}")

# Determine the top 5 most commonly used programming languages for each year
print("Top 5 most commonly used programming languages per year:")
for year in sorted(year_stats.keys(), reverse=True):
    stats = year_stats[year]
    sorted_languages = sorted(stats['language_stats'].items(), key=lambda item: item[1], reverse=True)
    top_5_languages = sorted_languages[:5]
    print(f"Year: {year}")
    for language, count in top_5_languages:
        print(f"  {language}: {count}")

# Plot the distribution of programming languages
grouped_counts = {
    'Python': 0,
    'C++': 0,
    'Java': 0,
    'MATLAB': 0,
    'Julia': 0,
    'Perl': 0,
    'Scala': 0,
    'JavaScript': 0,
    'Rust': 0,
    'Assembly': 0,
    'No programming languages found.': 0,
    'Others': 0
}

for language, count in language_counts.items():
    if language.lower() == 'python':
        grouped_counts['Python'] += count
    elif language.lower() == 'c++':
        grouped_counts['C++'] += count
    elif language.lower() == 'java':
        grouped_counts['Java'] += count
    elif language.lower() == 'matlab':
        grouped_counts['MATLAB'] += count
    elif language.lower() == 'julia':
        grouped_counts['Julia'] += count
    elif language.lower() == 'perl':
        grouped_counts['Perl'] += count
    elif language.lower() == 'scala':
        grouped_counts['Scala'] += count
    elif language.lower() == 'javascript':
        grouped_counts['JavaScript'] += count
    elif language.lower() == 'rust':
        grouped_counts['Rust'] += count
    elif language.lower() == 'assembly':
        grouped_counts['Assembly'] += count
    elif language.lower() == 'no programming languages found.':
        grouped_counts['No programming languages found.'] += count
    else:
        grouped_counts['Others'] += count
        others_languages.append(language)  # Collect languages in 'Others'

grouped_languages = list(grouped_counts.keys())
grouped_counts_values = list(grouped_counts.values())

plt.figure(figsize=(15, 7))
plt.bar(grouped_languages, grouped_counts_values, color='skyblue')
plt.xlabel('Programming Languages')
plt.ylabel('Count')
plt.title('Distribution of Programming Languages in the Dataset')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Print the most common bi-grams and tri-grams
print("Most common bi-grams:")
for bi_gram, count in bi_gram_counter.most_common(10):
    print(f"{bi_gram}: {count}")

print("\nMost common tri-grams:")
for tri_gram, count in tri_gram_counter.most_common(10):
    print(f"{tri_gram}: {count}")

# Save the languages found in 'Others' to a file
with open('languages_in_others.txt', 'w') as file:
    for language in others_languages:
        file.write(f"{language}\n")
