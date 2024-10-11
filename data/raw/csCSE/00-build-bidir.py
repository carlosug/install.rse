import csv

# Read the contents of the bidir_dataset.csv file
with open('data/raw/csCSE/bidir_dataset.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Create a set to store unique repositories
unique_repositories = set()

# Create a list to store duplicate repositories
duplicate_repositories = []

# Iterate over the data and count unique and duplicate repositories
for item in data:
    repository = item['url']
    if repository in unique_repositories:
        duplicate_repositories.append(repository)
    else:
        unique_repositories.add(repository)

# Count the number of unique repositories
num_unique_repositories = len(unique_repositories)

# Count the number of duplicate repositories
num_duplicate_repositories = len(duplicate_repositories)

# Count the number of rows in the CSV data
num_rows = len(data)

print(f"Number of unique repositories: {num_unique_repositories}")
print(f"Number of duplicate repositories: {num_duplicate_repositories}")
print(f"Number of rows in the CSV data: {num_rows}")

# Print the list of duplicate repositories
print("List of duplicate repositories:")
for repo in duplicate_repositories:
    print(repo)

# Create a new CSV file with unique repositories - this is the input for somef
with open('data/processed/00_bidir_dataset_unique.csv', 'w', newline='') as file:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for item in data:
        if item['url'] in unique_repositories:
            writer.writerow(item)
            unique_repositories.remove(item['url'])
            # Count and list repositories with URLs that do not contain 'https://github'
            non_github_repositories = [item['url'] for item in data if 'https://github' not in item['url'] and 'http://github' not in item['url']]
            num_non_github_repositories = len(non_github_repositories)
    print(f"Number of non-GitHub repositories: {num_non_github_repositories}")
            # Create a new CSV file with non-GitHub repositories
    with open('data/processed/00_non_github_repositories.csv', 'w', newline='') as non_github_file:
        non_github_writer = csv.writer(non_github_file)
        non_github_writer.writerow(['url'])  # Assuming 'url' is the only field needed
        for repo in non_github_repositories:
                non_github_writer.writerow([repo])