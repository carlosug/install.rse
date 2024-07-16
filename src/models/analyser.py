import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Sample README instructions
readme_instructions = {
    "repo1": "## Installation\npip install numpy\npip install pandas\n\n## Configuration\nAdd to PATH\n",
    "repo2": "## Install\nconda install scikit-learn\n\n## Setup\npip install seaborn",
    "repo3": "## Getting Started\npip install tensorflow\ngit clone https://github.com/example/repo.git\ncd repo\npython setup.py install",
    "repo4": "## Quick Start\npip install requests"
}

# Extract and categorize sections
def extract_sections(text):
    sections = re.findall(r'## [\w\s]+', text)
    instructions = re.split(r'## [\w\s]+', text)[1:]
    return dict(zip(sections, instructions))

section_relationships = defaultdict(list)
for repo, instruction in readme_instructions.items():
    sections = extract_sections(instruction)
    for section, steps in sections.items():
        steps = steps.split('\n')
        for i in range(len(steps) - 1):
            if steps[i] and steps[i+1]:
                section_relationships[section].append((steps[i], steps[i+1]))

# Create and visualize networks for each section
for section, relationships in section_relationships.items():
    G = nx.DiGraph()
    for source, target in relationships:
        G.add_edge(source.strip(), target.strip())

    plt.figure(figsize=(10, 8))
    nx.draw_networkx(G, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
    plt.title(f'Structure of {section} Section')
    plt.show()


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Extract all installation methods
install_methods = []
for instruction in readme_instructions.values():
    sections = extract_sections(instruction)
    for section, steps in sections.items():
        install_methods.append(steps)

# Vectorize and cluster installation methods
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(install_methods)
kmeans = KMeans(n_clusters=5)  # Adjust the number of clusters as needed
kmeans.fit(X)

# Output cluster centers and labels
print("Cluster Centers:", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)

from collections import Counter

# Count labels to find the most common clusters
label_counts = Counter(kmeans.labels_)
most_common_labels = label_counts.most_common(3)  # Top 3 typical methods

for label, count in most_common_labels:
    print(f"Cluster {label} (count: {count}):")
    for i, method in enumerate(install_methods):
        if kmeans.labels_[i] == label:
            print(method)

# Define categories based on clusters
categories = {label: [] for label in range(kmeans.n_clusters)}
for i, label in enumerate(kmeans.labels_):
    categories[label].append(install_methods[i])

# Summarize categories
for label, methods in categories.items():
    print(f"Category {label}:")
    for method in methods[:3]:  # Show a few examples from each category
        print(method)


from sklearn.feature_extraction.text import CountVectorizer

# Combine all installation methods
all_install_methods = ' '.join(install_methods)

# Vectorize and analyze common phrases
vectorizer = CountVectorizer(ngram_range=(1, 2), stop_words='english')
X = vectorizer.fit_transform([all_install_methods])
common_phrases = vectorizer.get_feature_names_out()
frequencies = X.toarray().sum(axis=0)

# Find the most common phrases
phrase_freq = dict(zip(common_phrases, frequencies))
sorted_phrases = sorted(phrase_freq.items(), key=lambda x: x[1], reverse=True)[:10]
print("Common patterns:", sorted_phrases)



# Define categories based on keywords
categories = {'server': [], 'library': []}

for repo, instruction in readme_instructions.items():
    if 'server' in instruction.lower():
        categories['server'].append(instruction)
    elif 'library' in instruction.lower():
        categories['library'].append(instruction)

# Summarize categories
for category, methods in categories.items():
    print(f"{category.capitalize()} installation methods:")
    for method in methods[:3]:  # Show a few examples from each category
        print(method)
