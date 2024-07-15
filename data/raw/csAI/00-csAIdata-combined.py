import csv
import os

# List of CSV file paths to combine
csv_files = [
    '/Users/ccugutrillague/Documents/perso/doctorado/projects/install.rse/data/raw/csAI/2022_csAi_roberta_output.csv',
    '/Users/ccugutrillague/Documents/perso/doctorado/projects/install.rse/data/raw/csAI/2022_csAi_scibert_out.csv',
    '/Users/ccugutrillague/Documents/perso/doctorado/projects/install.rse/data/raw/csAI/2023_csAi_roberta_output.csv',
    '/Users/ccugutrillague/Documents/perso/doctorado/projects/install.rse/data/raw/csAI/2023_csAi_scibert_output.csv'
]

# Path for the combined output CSV file
output_file_path = 'data/processed/combined_csAI.csv'  # Update with actual output file path

# Set to store encountered links
encountered_links = set()

# Open the output file in write mode
with open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file:
    csv_writer = csv.writer(output_file)
    # Optionally write a header row, if your CSVs have headers
    csv_writer.writerow(['DOI', 'Link'])

    for file_path in csv_files:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)  # Skip the header row of each CSV file
            
            # Variables to store statistics
            total_links = 0
            unique_links = 0

            for row in csv_reader:
                if row[1] and row[1] not in encountered_links:  # Check if the second column (Link) is not empty and not a duplicate
                    csv_writer.writerow(row)  # Write each row to the output file
                    encountered_links.add(row[1])  # Add the link to the set of encountered links
                    unique_links += 1

                total_links += 1

            print(f"Statistics for file: {file_path}")
            print(f"Total links: {total_links}")
            print(f"Unique links: {unique_links}")
            print()  # Print an empty line for separation
