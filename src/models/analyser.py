import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Step 1: Read the JSON File
with open('installation_features.json', 'r') as file:
    data = json.load(file)

# Step 2: Parse the JSON Content
installation_instructions = []
for project in data.values():
    for item in project:
        if isinstance(item, dict) and 'result' in item and 'value' in item['result']:
            instructions = item['result']['value']
            installation_instructions.append(instructions)

# Step 3: Preprocess the Installation Instructions
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

preprocessed_instructions = [preprocess_text(instr) for instr in installation_instructions]

# Step 4: Convert Installation Instructions to TF-IDF Vectors
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(preprocessed_instructions)

# Step 5: Apply Clustering
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X)

# Step 6: Output and Visualization
print("Cluster assignments:", clusters)

# Save cluster assignments
with open('cluster_assignments.txt', 'w') as f:
    for assignment in clusters:
        f.write(f'{assignment}\n')

# Visualization using t-SNE
tsne = TSNE(n_components=2, perplexity=50, n_iter=3000, random_state=42)
X_tsne = tsne.fit_transform(X.toarray())

plt.figure(figsize=(12, 8))
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=clusters)
plt.title('Clusters of Installation Instructions')
plt.xlabel('t-SNE feature 1')
plt.ylabel('t-SNE feature 2')
plt.colorbar()
plt.show()