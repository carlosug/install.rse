# Example usage of the extract function from extractor.py
import nltk
nltk.download('omw-1.4')


# Assuming the extractor.py script is in the same directory and has been imported correctly
from extractor import extract

# Define the parameters for the extract function
repos_txt_file = "./02_urls_not_found.txt"  # as previous extractor stop, here I extract the rest of list (I took out: https://github.com/mdrafiqulrabin/kconfig  as I got bugs)
output_directory = "./01.1-extracted_metadata-c"  # Directory where the other extracted metadata will be saved
use_inspect4py = False  # Set to True to use inspect4py for additional analysis
verbose = False  # Set to True for more detailed output during the extraction process
keep = False  # Set to True to keep the existing output directory, False will delete it before extraction (changed - before was keep_output_dir)

# Call the extract function with the defined parameters
extract(repos_txt_file, output_directory, use_inspect4py, verbose, keep)