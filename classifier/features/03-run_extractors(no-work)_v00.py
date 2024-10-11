import nltk
import os
import json
from extractor import extract
from extractor_install import extract_installation_features_to_json

# Download necessary NLTK data
nltk.download('omw-1.4')

# Define the parameters for the extract function
repos_txt_file = "./link.txt"  # This file should contain a list of GitHub URLs, one per line
output_directory = "./extracted_metadata"  # Directory where the extracted metadata will be saved
use_inspect4py = False  # Set to True to use inspect4py for additional analysis
verbose = True  # Set to True for more detailed output during the extraction process
keep = False  # Set to True to keep the existing output directory, False will delete it before extraction

# Call the extract function with the defined parameters
print("Starting extraction process...")
extract(repos_txt_file, output_directory, use_inspect4py, verbose, keep)
print("Extraction process completed.")

# Check if the output directory was created
if not os.path.exists(output_directory):
    raise FileNotFoundError(f"The directory {output_directory} was not created by the extract function.")
else:
    print(f"The directory {output_directory} was successfully created.")

# Define the parameters for the extract_installation_features_to_json function
extracted_metadata_folder = 'extracted_metadata'
output_json_file = 'installation_features.json'  # Output file for the extracted installation features

# Call the extract_installation_features_to_json function with the defined parameters
print("Starting extraction of installation features...")
extract_installation_features_to_json(extracted_metadata_folder, output_json_file)
print("Extraction of installation features completed.")