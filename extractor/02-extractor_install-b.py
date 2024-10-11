import json
import os

def count_json_files(folder_path):
    """
    Counts the number of JSON files in the specified folder.
    
    Parameters:
    folder_path (str): The path to the folder containing JSON files.
    
    Returns:
    int: The number of JSON files found in the folder.
    """
    return len([filename for filename in os.listdir(folder_path) if filename.endswith('.json')])

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

    # Count the number of JSON files in the folder
    json_file_count = count_json_files(extracted_metadata_folder)
    print(f"Number of JSON files found: {json_file_count}")

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
                code_repository = data.get('code_repository', 'No code repository found.')
                
                # Add the extracted information to the dictionary with a unique numeric ID
                installation_features[unique_id] = {
                    'filename': filename,
                    'code_repository': code_repository,
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
extracted_metadata_folder = 'extractor/01-extracted_metadata-b' #folder with JSON files containing metadata
output_json_file = 'extractor/02_installation_readmes-b.json' #input file for computing clustering
extract_installation_features_to_json(extracted_metadata_folder, output_json_file)