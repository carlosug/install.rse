import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# Step 1: Load and Preprocess Data
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

with open('02_combined_installation_readmes.json', 'r') as file:
    data = json.load(file)

installation_instructions = [preprocess_text(item['result']['value']) for project in data.values() for item in project if isinstance(item, dict) and 'result' in item]

# Step 2: Extract Features
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X = vectorizer.fit_transform(installation_instructions)

# Step 3: Topic Modeling
lda = LatentDirichletAllocation(n_components=5, random_state=0)
lda.fit(X)

# Step 4: Network Analysis
G = nx.Graph()
methods = ['pip', 'conda', 'docker', 'git', 'cmake']
for method in methods:
    G.add_node(method)

for text in installation_instructions:
    present_methods = [method for method in methods if method in text]
    for i in range(len(present_methods)):
        for j in range(i + 1, len(present_methods)):
            G.add_edge(present_methods[i], present_methods[j])

# Step 5: Basic Statistics
print(f"Distinct installation methods: {len(methods)}")

# Step 6: Clustering
clustering = DBSCAN(eps=0.5, min_samples=2).fit(X.toarray())
labels = clustering.labels_
num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(f"Number of clusters: {num_clusters}")

# Step 7: Visualization
# Topic Modeling Visualization
for topic_idx, topic in enumerate(lda.components_):
    print(f"Topic #{topic_idx+1}:")
    print(" ".join([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[:-10 - 1:-1]]))

# Network Analysis Visualization
plt.figure(figsize=(10, 10))
nx.draw_networkx(G, with_labels=True, node_size=2000, node_color="skyblue", font_size=20)
plt.title("Network of Installation Methods")
plt.show()