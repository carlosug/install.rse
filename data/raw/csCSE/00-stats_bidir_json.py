import json

# Read the contents of the bidir.json file
with open('data/raw/csCSE/bidir.json', 'r') as file:
    data = json.load(file)

# Create a set to store unique repositories
unique_repositories = set()

# Create a list to store duplicate repositories
duplicate_repositories = []

# Iterate over the data and count unique and duplicate repositories
for item in data.values():
    for repo in item:
        repository = repo['url']
        if repository in unique_repositories:
            duplicate_repositories.append(repository)
        else:
            unique_repositories.add(repository)

# Count the number of unique repositories
num_unique_repositories = len(unique_repositories)

# Count the number of duplicate repositories
num_duplicate_repositories = len(duplicate_repositories)

# Count the number of keys in the JSON data
num_keys = len(data)

print(f"Number of unique repositories: {num_unique_repositories}")
print(f"Number of duplicate repositories: {num_duplicate_repositories}")
print(f"Number of keys in the JSON data: {num_keys}")