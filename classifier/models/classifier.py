import json

# File paths
input_json_file = '02_installation_readmes.json'
output_txt_file = 'installation_instructions.txt'

# Read data from the JSON file
with open(input_json_file, 'r') as file:
    json_data = json.load(file)

# Extract installation instructions
installation_instructions = []
for entry in json_data.values():
    if 'results' in entry and 'installation_instructions' in entry['results']:
        for instruction in entry['results']['installation_instructions']:
            if 'result' in instruction and 'value' in instruction['result']:
                installation_instructions.append(instruction['result']['value'])

# Save the installation instructions to a text file
with open(output_txt_file, 'w') as file:
    for instruction in installation_instructions:
        file.write(instruction + '\n')

print(f"Installation instructions have been saved to {output_txt_file}.")