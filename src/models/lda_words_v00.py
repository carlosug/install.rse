import json
import re
import gensim
import gensim.corpora as corpora
from gensim.models import Phrases
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import nltk
import pyLDAvis
import pyLDAvis.gensim_models
import os

# Download NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english')).union(set(ENGLISH_STOP_WORDS))
lemmatizer = WordNetLemmatizer()

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Function to tokenize and clean text
def tokenize_and_clean(text):
    tokens = simple_preprocess(text, deacc=True)
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

# Load the JSON file
input_file_path = 'installation_readmes.json'
with open(input_file_path, 'r') as file:
    data = json.load(file)

# Extract and preprocess installation instructions
installation_instructions = []
repos = []

for repo_id, repo in data.items():
    if not repo:
        continue  # Skip if no items found

    combined_instructions = ""
    for item in repo.get('installation_instructions', []):
        if isinstance(item, dict) and 'result' in item and 'value' in item['result']:
            combined_instructions += item['result']['value'] + " "
    
    if combined_instructions:
        preprocessed_text = preprocess_text(combined_instructions.strip())
        tokens = tokenize_and_clean(preprocessed_text)
        installation_instructions.append(tokens)
        repos.append(repo_id)

# Create bigrams
bigram = Phrases(installation_instructions, min_count=5, threshold=100)
bigram_mod = gensim.models.phrases.Phraser(bigram)
installation_instructions = [bigram_mod[doc] for doc in installation_instructions]

# Create dictionary and corpus
id2word = corpora.Dictionary(installation_instructions)
corpus = [id2word.doc2bow(text) for text in installation_instructions]

# Apply LDA
num_topics = 4  # Adjust the number of topics as needed
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                            id2word=id2word,
                                            num_topics=num_topics,
                                            random_state=100,
                                            update_every=1,
                                            chunksize=10,
                                            passes=10,
                                            alpha='auto',
                                            per_word_topics=True)

# Print the topics
topics = lda_model.print_topics(num_words=10)
for topic in topics:
    print(topic)

# Visualize the topics with customizations
lda_display = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word, sort_topics=False)

# Customize the plot size
pyLDAvis.display(lda_display)

# Save the visualization to an HTML file
output_file = 'lda-words.html'
pyLDAvis.save_html(lda_display, output_file)
print(f"LDA visualization saved as {output_file}")

# Optionally, you can edit the generated HTML file to customize CSS styles
with open(output_file, 'r') as file:
    html_content = file.read()

# Example: Modify the background color of the plot
html_content = html_content.replace('<style>', '<style> body { background-color: #f0f0f0; } ')

with open(output_file, 'w') as file:
    file.write(html_content)