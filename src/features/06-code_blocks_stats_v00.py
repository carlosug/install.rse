import json
from collections import defaultdict, Counter
from tabulate import tabulate
import matplotlib.pyplot as plt

# Initialize year_stats with default values
year_stats = defaultdict(lambda: {
    'total_count': 0,
    'with_code_blocks': 0,
    'without_code_blocks': 0,
    'keywords': Counter()
})

def is_code_block(line):
    return line.startswith("```") or line.startswith("`")

def extract_keywords(code_block):
    # Simple keyword extraction: split by whitespace and filter out common non-keyword characters
    keywords = code_block.split()
    return [keyword.strip('`.,()[]{}<>:;\'"') for keyword in keywords]

# Load the JSON file
with open('installation_readmes-01.json', 'r') as file:
    data = json.load(file)

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
                            if not in_code_block:
                                # End of code block, extract keywords
                                keywords = extract_keywords(' '.join(code_block_lines))
                                year_stats[year]['keywords'].update(keywords)
                                code_block_lines = []
                        elif in_code_block:
                            code_block_lines.append(line)
                    if in_code_block:
                        # Handle case where code block is not properly closed
                        keywords = extract_keywords(' '.join(code_block_lines))
                        year_stats[year]['keywords'].update(keywords)
    
    if has_code_block:
        year_stats[year]['with_code_blocks'] += 1
    else:
        year_stats[year]['without_code_blocks'] += 1

# Prepare data for the table
table_data = []
for year, stats in sorted(year_stats.items(), reverse=True):
    total_count = stats['total_count']
    with_code_blocks = stats['with_code_blocks']
    without_code_blocks = stats['without_code_blocks']
    
    if total_count > 0:
        with_code_blocks_percentage = (with_code_blocks / total_count) * 100
        without_code_blocks_percentage = (without_code_blocks / total_count) * 100
    else:
        with_code_blocks_percentage = 0
        without_code_blocks_percentage = 0
    
    table_data.append([
        year,
        total_count,
        with_code_blocks,
        f"{with_code_blocks_percentage:.2f}%",
        without_code_blocks,
        f"{without_code_blocks_percentage:.2f}%"
    ])

# Print the table
headers = ["Year", "Total Count", "With Code Blocks", "With Code Blocks (%)", "Without Code Blocks", "Without Code Blocks (%)"]
print(tabulate(table_data, headers, tablefmt="grid"))

# Plot the distribution of the top 10 keywords per year
for year, stats in sorted(year_stats.items(), reverse=True):
    keywords = stats['keywords']
    if keywords:
        top_keywords = keywords.most_common(10)
        labels, counts = zip(*top_keywords)
        plt.figure(figsize=(10, 5))
        plt.bar(labels, counts)
        plt.title(f"Top 10 Keywords in Code Blocks for {year}")
        plt.xlabel("Keywords")
        plt.ylabel("Counts")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Assuming year_stats is already populated as per the previous code

# Get the keywords for the year 2013
keywords_2013 = year_stats.get('2013', {}).get('keywords', Counter())

# Get the top 10 keywords
top_keywords_2013 = keywords_2013.most_common(10)

# Print the top 10 keywords
print("Top 10 Keywords in Code Blocks for 2013:")
for keyword, count in top_keywords_2013:
    print(f"{keyword}: {count}")