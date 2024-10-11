import json
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import ttest_ind
import numpy as np

# Load the JSON file
output = "extractor/02_combined_installation_readmes.json"

# Load the JSON file
with open(output, 'r') as file:
    data = json.load(file)

# Initialize year_stats with default values
year_stats = defaultdict(lambda: {
    'total_count': 0,
    'with_code_blocks': 0,
    'without_code_blocks': 0,
    'keywords': Counter(),
    'code_block_lengths': []
})

def is_code_block(line):
    return line.startswith("```") or line.startswith("`")

def extract_keywords(code_block):
    # Simple keyword extraction: split by whitespace and filter out common non-keyword characters
    keywords = code_block.split()
    return [keyword.strip('`.,()[]{}<>:;\'"') for keyword in keywords]

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
    
    # Check for installation instructions
    installation_instructions = repo.get('installation_instructions', [])
    if isinstance(installation_instructions, str) and installation_instructions == "No installation instructions found.":
        continue  # Skip this repository
    
    # Update total count for the year
    year_stats[year]['total_count'] += 1
    
    # Check for code blocks and extract keywords
    has_code_block = False
    if isinstance(installation_instructions, list):
        for instruction in installation_instructions:
            if isinstance(instruction, dict):
                value = instruction.get('result', {}).get('value', '')
                if "```" in value or "`" in value:
                    has_code_block = True
                    code_block_lines = []
                    in_code_block = False
                    for line in value.split('\n'):
                        if is_code_block(line):
                            in_code_block = not in_code_block
                            if not in_code_block and code_block_lines:
                                # End of code block, extract keywords and calculate mean length
                                keywords = extract_keywords(' '.join(code_block_lines))
                                year_stats[year]['keywords'].update(keywords)
                                mean_length = np.mean([len(word) for word in ' '.join(code_block_lines).split()])
                                if not np.isnan(mean_length):
                                    year_stats[year]['code_block_lengths'].append(mean_length)
                                code_block_lines = []
                        elif in_code_block:
                            code_block_lines.append(line)
                    if in_code_block and code_block_lines:
                        # Handle case where code block is not properly closed
                        keywords = extract_keywords(' '.join(code_block_lines))
                        year_stats[year]['keywords'].update(keywords)
                        mean_length = np.mean([len(word) for word in ' '.join(code_block_lines).split()])
                        if not np.isnan(mean_length):
                            year_stats[year]['code_block_lengths'].append(mean_length)
    
    if has_code_block:
        year_stats[year]['with_code_blocks'] += 1
    else:
        year_stats[year]['without_code_blocks'] += 1

# Prepare data for plotting
plot_data = []
for year, stats in year_stats.items():
    for length in stats['code_block_lengths']:
        plot_data.append({'Year': year, 'Mean Length': length})

df = pd.DataFrame(plot_data)

# Replace zeros with the minimum positive value for plotting
min_positive = df['Mean Length'].replace(0, np.nan).min()
df['Mean Length'] = df['Mean Length'].replace(0, min_positive)

# Perform t-tests and annotate p-values
years = df['Year'].unique()
p_values = {}
for i in range(len(years)):
    for j in range(i + 1, len(years)):
        year1 = years[i]
        year2 = years[j]
        data1 = df[df['Year'] == year1]['Mean Length']
        data2 = df[df['Year'] == year2]['Mean Length']
        t_stat, p_val = ttest_ind(data1, data2, equal_var=False)
        p_values[(year1, year2)] = p_val

# Create the box plot
plt.figure(figsize=(12, 8))
sns.boxplot(x='Year', y='Mean Length', data=df, showfliers=True)
plt.xlabel('Year')
plt.ylabel('Mean Length')
plt.title('Distribution of Mean Length of Code Blocks by Year')

# Annotate p-values
for (year1, year2), p_val in p_values.items():
    plt.annotate(f'p-value ({year1} vs {year2}): {p_val:.2e}', xy=(0.5, 0.95), xycoords='axes fraction', ha='center', va='top', fontsize=10, color='red')

plt.tight_layout()
plt.show()