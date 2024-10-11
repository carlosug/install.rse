# Define a function to calculate complexity score based on the number of steps and types of commands
import re
def calculate_complexity_score(instruction):
    steps = instruction.split('\n')
    num_steps = len(steps)
    command_types = len(set(re.findall(r'\b(pip|conda|brew|apt-get|yum|git|python)\b', instruction)))
    return num_steps + command_types

# Sample README instructions
readme_instructions = {
    "repo1": "pip install numpy\npip install pandas",
    "repo2": "conda install scikit-learn\npip install seaborn\npip install tensorflow\napt-get install libboost-all-dev",
    "repo3": "git clone https://github.com/example/repo.git\ncd repo\npython setup.py install",
    "repo4": "pip install requests"
}

# Calculate complexity scores
complexity_scores = {repo: calculate_complexity_score(instruction) for repo, instruction in readme_instructions.items()}
print(complexity_scores)

# Define threshold for high and low complexity
threshold = 5
high_complexity_repos = {repo: instruction for repo, instruction in readme_instructions.items() if complexity_scores[repo] > threshold}
low_complexity_repos = {repo: instruction for repo, instruction in readme_instructions.items() if complexity_scores[repo] <= threshold}

print("High Complexity Repos:", high_complexity_repos)
print("Low Complexity Repos:", low_complexity_repos)

# Extract relationships (commands and libraries) for high and low complexity repos
def extract_command_library_pairs(text):
    pairs = []
    commands = re.findall(r'\b(?:pip|conda|brew|apt-get|yum|git|python)\b', text)
    libraries = re.findall(r'\b[a-zA-Z0-9_\-]+\b', text)
    for i in range(len(commands)):
        if i < len(libraries):
            pairs.append((commands[i], libraries[i]))
    return pairs

high_relationships = []
for instruction in high_complexity_repos.values():
    high_relationships.extend(extract_command_library_pairs(instruction))

low_relationships = []
for instruction in low_complexity_repos.values():
    low_relationships.extend(extract_command_library_pairs(instruction))

print("High Complexity Relationships:", high_relationships)
print("Low Complexity Relationships:", low_relationships)

import networkx as nx
import matplotlib.pyplot as plt

# Create and draw graphs for high and low complexity
G_high = nx.DiGraph()
for source, target in high_relationships:
    G_high.add_edge(source, target)

G_low = nx.DiGraph()
for source, target in low_relationships:
    G_low.add_edge(source, target)

plt.figure(figsize=(10, 8))
nx.draw_networkx(G_high, with_labels=True, node_size=700, node_color='lightgreen', font_size=10, font_weight='bold', edge_color='gray')
plt.title('High Complexity Installation Network')
plt.show()

plt.figure(figsize=(10, 8))
nx.draw_networkx(G_low, with_labels=True, node_size=700, node_color='lightcoral', font_size=10, font_weight='bold', edge_color='gray')
plt.title('Low Complexity Installation Network')
plt.show()


import pandas as pd
import scipy.stats
from scipy.stats import ttest_ind

# Create a DataFrame for statistical analysis
data = {
    "repo": list(readme_instructions.keys()),
    "complexity_score": list(complexity_scores.values()),
    "group": ["high" if complexity_scores[repo] > threshold else "low" for repo in readme_instructions.keys()]
}

df = pd.DataFrame(data)
print(df)

# Statistical analysis
high_complexity_scores = df[df['group'] == 'high']['complexity_score']
low_complexity_scores = df[df['group'] == 'low']['complexity_score']

# T-test to compare the means of complexity scores
t_stat, p_value = ttest_ind(high_complexity_scores, low_complexity_scores)
print(f"T-test results: t_stat = {t_stat}, p_value = {p_value}")


