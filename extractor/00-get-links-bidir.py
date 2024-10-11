import csv

input_file = "data/processed/00_bidir_dataset_unique.csv"
output_file = "data/processed/somef-data/00_output_without_duplicated.txt"
duplicates_file = "data/processed/somef-data/00_duplicates.txt"
no_github_file = "data/processed/somef-data/00_non_github_repositories.txt"

links = []
all_links = []

with open(input_file, "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        link = row["url"]
        if link.startswith("github"):
            link = "https://" + link
        if link.startswith("https://www.github"):
            link = link.replace("https://www.github.com", "https://github.com")
        all_links.append(link)

# Identify duplicates
unique_links = set()
duplicates = set()
for link in all_links:
    if link in unique_links:
        duplicates.add(link)
    else:
        unique_links.add(link)

# Write duplicates to duplicates.txt
with open(duplicates_file, "w") as file:
    for link in duplicates:
        file.write(link + "\n")

# Remove non-GitHub links (https://doi.org or https://gitlab.com)
filtered_links = set()
for link in unique_links:
    if "github.com" in link:
        filtered_links.add(link)

# Write non-GitHub links to non_github_repositories.txt
with open(no_github_file, "w") as file:
    for link in unique_links:
        if "github.com" not in link:
            file.write(link + "\n")

# Update unique_links to only contain GitHub links
unique_links = filtered_links
# Remove duplicates from the links list
links = list(unique_links)

# Write unique links to output1.txt
with open(output_file, "w") as file:
    for link in links:
        file.write(link + "\n")

print("Text file with links generated successfully in file name:", output_file, "with", len(unique_links), "unique_urls")
print("Number of duplicates in {input_file}:", len(duplicates))
# Print number of non-GitHub repositories
with open(no_github_file, "r") as file:
    non_github_links = file.readlines()
print("Number of non-GitHub repositories:", len(non_github_links))