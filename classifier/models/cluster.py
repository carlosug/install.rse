# Data Collection and Preprocessing
import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

# Fetch README files using GitHub API
def fetch_readme(repo):
    url = f"https://api.github.com/repos/{repo}/readme"
    headers = {'Accept': 'application/vnd.github.v3.raw'}
    response = requests.get(url, headers=headers)
    return response.text if response.status_code == 200 else None

# Preprocess the text data
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)  # Remove HTML tags
    text = re.sub(r'[^a-z\s]', ' ', text)  # Remove special characters
    return text

# Example repositories
repos = ["numpy/numpy", "pandas-dev/pandas"]
readmes = [preprocess_text(fetch_readme(repo)) for repo in repos]

df = pd.DataFrame({"repository": repos, "readme": readmes})

# Feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
X = vectorizer.fit_transform(df['readme'])

# Convert to DataFrame
tfidf_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

# clustering
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
df['cluster'] = kmeans.labels_

# Topic Modeling

from sklearn.decomposition import LatentDirichletAllocation

lda = LatentDirichletAllocation(n_components=5, random_state=0)
lda.fit(X)

# Display topics
for idx, topic in enumerate(lda.components_):
    print(f"Topic {idx}:")
    print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])

# Visualizing the clusters
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Generate word cloud for each cluster
for cluster in df['cluster'].unique():
    text = ' '.join(df[df['cluster'] == cluster]['readme'])
    wordcloud = WordCloud(width=800, height=400).generate(text)
    
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Cluster {cluster} Word Cloud')
    plt.show()



