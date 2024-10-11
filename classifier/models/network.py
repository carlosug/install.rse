# RQ1: Which commands or libraries are the most central in the installation processes?
import re
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

# Sample preprocessed data
# Assuming readme_instructions is a list of strings containing installation sections from README files
readme_instructions = [
    "pip install numpy\npip install pandas\nconda install scikit-learn",
    "git clone https://github.com/example/repo.git\ncd repo\npython setup.py install"
]

# Function to extract relationships
def extract_relationships(text):
    commands = re.findall(r'\b(?:pip|conda|brew|apt-get|yum|install|clone|setup)\b', text)
    libraries = re.findall(r'\b[a-zA-Z0-9_\-]+\b', text)
    relationships = []
    for i in range(len(commands) - 1):
        relationships.append((commands[i], commands[i+1]))
    return relationships

# Extract relationships from all instructions
all_relationships = []
for instruction in readme_instructions:
    all_relationships.extend(extract_relationships(instruction))

# Create a directed graph
G = nx.DiGraph()
for source, target in all_relationships:
    G.add_edge(source, target)

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# Display top nodes by degree centrality
top_degree_nodes = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
print("Top nodes by degree centrality:", top_degree_nodes)

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw_networkx(G, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title('Installation Instructions Network')
plt.show()

# RQ2: What distinct communities or clusters of commands and libraries exist within the installation instructions?

from collections import Counter

# Remove a node and analyze the impact on the network
node_to_remove = "pip"
G_removed = G.copy()
G_removed.remove_node(node_to_remove)

# Draw the graph after removal
plt.figure(figsize=(10, 8))
nx.draw_networkx(G_removed, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title(f'Installation Network after Removing {node_to_remove}')
plt.show()

# Analyze the impact
original_components = nx.number_connected_components(G.to_undirected())
new_components = nx.number_connected_components(G_removed.to_undirected())
print(f"Number of components before removal: {original_components}")
print(f"Number of components after removal: {new_components}")



