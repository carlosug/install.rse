import json
import re
from collections import defaultdict, Counter
from tabulate import tabulate
import matplotlib.pyplot as plt
from urllib.parse import urlparse

# Initialize year_stats with default values
year_stats = defaultdict(lambda: {
    'total_count': 0,
    'with_hyperlinks': 0,
    'without_hyperlinks': 0,
    'keywords': Counter(),
    'hyperlinks_per_repo': [],
    'urls': Counter()
})

# Dictionary to store hyperlink counts per repository
repo_hyperlink_counts = {}

def find_hyperlinks(line):
    return re.findall(r'\[([^\]]+)\]\((http[^\)]+)\)', line)

def extract_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

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
    
    # Count hyperlinks
    hyperlink_count = 0
    if isinstance(installation_instructions, list):
        for instruction in installation_instructions:
            if isinstance(instruction, dict):
                value = instruction.get('result', {}).get('value', '')
                hyperlinks = find_hyperlinks(value)
                hyperlink_count += len(hyperlinks)
                
                # Extract and count domains
                for _, url in hyperlinks:
                    domain = extract_domain(url)
                    year_stats[year]['urls'][domain] += 1
    
    # Update hyperlink statistics
    if hyperlink_count > 0:
        year_stats[year]['with_hyperlinks'] += 1
    else:
        year_stats[year]['without_hyperlinks'] += 1
    
    # Store the hyperlink count per repository
    year_stats[year]['hyperlinks_per_repo'].append(hyperlink_count)
    repo_hyperlink_counts[repo_id] = hyperlink_count

# Prepare data for the domains table
domains_table_data = []
for year, stats in sorted(year_stats.items(), reverse=True):
    top_urls = stats['urls'].most_common(5)
    for url, count in top_urls:
        domains_table_data.append([year, url, count])

# Print the domains table
domains_headers = ["Year", "URL", "Count"]
print("\nTop 5 Most Popular Websites Encapsulated in Hyperlinks for Each Year:")
print(tabulate(domains_table_data, domains_headers, tablefmt="grid"))

# Prepare data for the table
table_data = []
for year, stats in sorted(year_stats.items(), reverse=True):
    total_count = stats['total_count']
    with_hyperlinks = stats['with_hyperlinks']
    without_hyperlinks = stats['without_hyperlinks']
    avg_hyperlinks_per_repo = sum(stats['hyperlinks_per_repo']) / len(stats['hyperlinks_per_repo']) if stats['hyperlinks_per_repo'] else 0
    
    if total_count > 0:
        with_hyperlinks_percentage = (with_hyperlinks / total_count) * 100
        without_hyperlinks_percentage = (without_hyperlinks / total_count) * 100
    else:
        with_hyperlinks_percentage = 0
        without_hyperlinks_percentage = 0
    
    table_data.append([
        year,
        total_count,
        with_hyperlinks,
        f"{with_hyperlinks_percentage:.2f}%",
        without_hyperlinks,
        f"{without_hyperlinks_percentage:.2f}%",
        f"{avg_hyperlinks_per_repo:.2f}"
    ])

# Print the table
headers = ["Year", "Total Count", "With Hyperlinks", "With Hyperlinks (%)", "Without Hyperlinks", "Without Hyperlinks (%)", "Avg Hyperlinks per Repo"]
print(tabulate(table_data, headers, tablefmt="grid"))

# Plot the distribution of the top 10 keywords per year
for year, stats in sorted(year_stats.items(), reverse=True):
    keywords = stats['keywords']
    if keywords:
        top_keywords = keywords.most_common(10)
        labels, counts = zip(*top_keywords)
        plt.figure(figsize=(10, 5))
        plt.bar(labels, counts)
        plt.title(f"Top 10 Keywords in Hyperlinks for {year}")
        plt.xlabel("Keywords")
        plt.ylabel("Counts")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()  # Ensure the plot is displayed

# Assuming year_stats is already populated as per the previous code

# Get the keywords for the year 2013
keywords_2013 = year_stats.get('2013', {}).get('keywords', Counter())

# Get the top 10 keywords
top_keywords_2013 = keywords_2013.most_common(10)

# Print the top 10 keywords
print("Top 10 Keywords in Hyperlinks for 2013:")
for keyword, count in top_keywords_2013:
    print(f"{keyword}: {count}")

# Generate a report of the repositories with the highest number of hyperlinks
sorted_repos = sorted(repo_hyperlink_counts.items(), key=lambda x: x[1], reverse=True)
top_repos = sorted_repos[:10]  # Get top 10 repositories

print("\nTop 10 Repositories with the Highest Number of Hyperlinks:")
for repo_id, count in top_repos:
    print(f"Repository ID: {repo_id}, Hyperlink Count: {count}")