import pandas as pd
import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import nltk
import seaborn as sns
import matplotlib.pyplot as plt

# Download NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Load the dataset
file_path = './repo_manual_annotation.csv'  # Replace with your actual dataset path
data = pd.read_csv(file_path)

# Convert 'Star' column to numeric, removing commas
data['Star'] = data['Star'].replace({',': ''}, regex=True).astype(float)

# Topic Modeling and Analysis of Headers
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_word_frequencies(header_texts):
    all_words = []
    for text in header_texts:
        if pd.notnull(text):
            preprocessed_text = preprocess_text(text)
            words = word_tokenize(preprocessed_text)
            words = [word for word in words if word not in stop_words]
            all_words.extend(words)
    word_counts = Counter(all_words)
    return word_counts

def extract_ngrams(text, num):
    preprocessed_text = preprocess_text(text)
    tokens = word_tokenize(preprocessed_text)
    tokens = [token for token in tokens if token.isalnum()]
    n_grams = ngrams(tokens, num)
    return [' '.join(grams) for grams in n_grams]

def get_ngram_frequencies(header_texts, num):
    all_ngrams = []
    for text in header_texts:
        if pd.notnull(text):
            ngrams_list = extract_ngrams(text, num)
            all_ngrams.extend(ngrams_list)
    ngram_counts = Counter(all_ngrams)
    return ngram_counts

header_columns = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
header_analysis = {}
bigram_analysis = {}
trigram_analysis = {}

for header in header_columns:
    header_texts = data[header].dropna().tolist()
    word_frequencies = get_word_frequencies(header_texts)
    bigram_frequencies = get_ngram_frequencies(header_texts, 2)
    trigram_frequencies = get_ngram_frequencies(header_texts, 3)
    header_analysis[header] = word_frequencies
    bigram_analysis[header] = bigram_frequencies
    trigram_analysis[header] = trigram_frequencies

# Create DataFrames for the heatmaps
heatmap_data = pd.DataFrame(header_analysis).fillna(0)
bigram_heatmap_data = pd.DataFrame(bigram_analysis).fillna(0)
trigram_heatmap_data = pd.DataFrame(trigram_analysis).fillna(0)

# Plot the heatmap for words
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=False, cmap="YlGnBu", cbar=True)
plt.title('Heatmap of Most Common Words in Headers')
plt.xlabel('Headers')
plt.ylabel('Words')
plt.savefig('headers_heatmap.png', bbox_inches='tight')
plt.show()

# Plot the heatmap for bi-grams
plt.figure(figsize=(12, 8))
sns.heatmap(bigram_heatmap_data, annot=False, cmap="YlGnBu", cbar=True)
plt.title('Heatmap of Most Common Bi-grams in Headers')
plt.xlabel('Headers')
plt.ylabel('Bi-grams')
plt.savefig('bigrams_heatmap.png', bbox_inches='tight')
plt.show()

# Plot the heatmap for tri-grams
plt.figure(figsize=(12, 8))
sns.heatmap(trigram_heatmap_data, annot=False, cmap="YlGnBu", cbar=True)
plt.title('Heatmap of Most Common Tri-grams in Headers')
plt.xlabel('Headers')
plt.ylabel('Tri-grams')
plt.savefig('trigrams_heatmap.png', bbox_inches='tight')
plt.show()

# Output the most common word for each header
for header, word_counts in header_analysis.items():
    most_common_word, _ = word_counts.most_common(1)[0] if word_counts else (None, None)
    print(f"The most common word in {header} is: {most_common_word}")

# Analysis of Common Installation Methods in Repositories with Highest Stars
# Define the threshold for the highest number of stars
top_star_threshold = data['Star'].quantile(0.95)  # Top 5% of repositories by stars

# Filter repositories with stars above the threshold
top_star_repos = data[data['Star'] >= top_star_threshold]

# Extract and count installation methods
installation_methods = top_star_repos['method_type'].dropna().str.split(', ').explode()
installation_method_counts = installation_methods.value_counts()

# Output the most common installation methods
print("\nCommon installation methods in repositories with the highest number of stars:")
print(installation_method_counts)