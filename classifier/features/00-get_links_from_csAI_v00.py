import csv

input_file = "../data/processed/combined_csAI.csv"
output_file = "output.txt"

links = []

with open(input_file, "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        link = row["Link"]
        if link.startswith("github"):
            link = "https://" + link
        links.append(link)

# Count the number of duplicates in the links list
duplicate_count = len(links) - len(set(links))

with open(output_file, "w") as file:
    for link in links:
        file.write(link + "\n")

print("Text file with links generated successfully!")
print("Number of duplicates:", duplicate_count)
