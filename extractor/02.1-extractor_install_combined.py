import json

# Paths to the JSON files
file1_path = 'extractor/02_installation_readmes-b.json' # first run for somef 865
file2_path = 'extractor/02_installation_readmes-c.json' # second run for somef 350
merged_file_path = 'extractor/02_combined_installation_readmes.json' # output file for the entire analysis
# Load JSON data from the files
# Load JSON data from the files
with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)

# Combine the data based on the 'filename' key
# Start by copying data1, then add non-conflicting entries from data2
merged_data = data1.copy()

for key, value in data2.items():
    # Check if the filename is unique, if yes, add the entry
    if not any(entry["filename"] == value["filename"] for entry in merged_data.values()):
        merged_data[str(len(merged_data))] = value

# Save the merged data to a new JSON file
with open(merged_file_path, 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=4)

print(f"Merged data saved to {merged_file_path}")
print(f"Number of entries in the 1st file: {len(data1)}")
print(f"Number of entries in the 2nd file: {len(data2)}")
print(f"Number of entries in the merged file: {len(merged_data)}")