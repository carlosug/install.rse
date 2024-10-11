import json
import os

def extract_installation_features_to_json(extracted_metadata_folder, output_json_file):
    """
    Extracts installation instructions, date_created, date_updated, and programming_languages from a list of JSON files 
    in the specified folder and saves them to a JSON file.
    
    Parameters:
    extracted_metadata_folder (str): The path to the folder containing JSON files with metadata.
    output_json_file (str): The path to the output JSON file where the results will be saved.
    """
    installation_features = {}

    # Initialize a counter for unique numeric IDs
    unique_id = 0

    # Iterate through each file in the specified folder
    for filename in os.listdir(extracted_metadata_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(extracted_metadata_folder, filename)
            
            # Open and load the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
                
                # Extract installation instructions
                installation_instructions = data.get('installation', 'No installation instructions found.')
                
                # Extract date_created, date_updated, and programming_languages
                date_created = data.get('date_created', 'No date_created found.')
                date_updated = data.get('date_updated', 'No date_updated found.')
                programming_languages = data.get('programming_languages', 'No programming languages found.')
                
                # Add the extracted information to the dictionary with a unique numeric ID
                installation_features[unique_id] = {
                    'filename': filename,
                    'installation_instructions': installation_instructions,
                    'date_created': date_created,
                    'date_updated': date_updated,
                    'programming_languages': programming_languages
                }
                
                # Increment the unique ID counter
                unique_id += 1

    # Save the extracted features to a JSON file
    with open(output_json_file, 'w') as outfile:
        json.dump(installation_features, outfile, indent=4)

# Example usage
extracted_metadata_folder = 'extracted_metadata'
output_json_file = 'installation_readmes-01.json' #input file for computing clustering
extract_installation_features_to_json(extracted_metadata_folder, output_json_file)