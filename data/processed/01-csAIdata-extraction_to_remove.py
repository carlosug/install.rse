import csv
import json
import os
import subprocess

# Define the path to the input CSV and output JSON files
input_csv_path = 'data/processed/combined_csAI.csv'
output_json_path = 'data/processed/extracted_categories.json'

# Define the output directory path
output_json_dir = 'data/processed'

# Pull the somef Docker image first to ensure it's available
docker_pull_command = ['docker', 'pull', 'kcapd/somef']
subprocess.run(docker_pull_command, check=True)

# Initialize a dictionary to hold the Link and extracted categories
results = {}

# Read the CSV file
with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        link = row['Link']  # Assuming 'Link' is the column name
        # Construct the Docker run command for each link
        # docker_run_command = ['somef describe -r ' + link + ' -o test.json -t 0.8'] ## doesnt work
        # Ensure the output directory exists
        os.makedirs(output_json_dir, exist_ok=True)
        
        # Define the path to the input CSV and output JSON file
        input_csv_path = 'data/processed/combined_csAI.csv'
        output_json_path = 'data/processed/extracted_data.json'
        
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_json_path)
        os.makedirs(output_dir, exist_ok=True)
        
        # Pull the somef Docker image first to ensure it's available
        # docker_pull_command = ['docker', 'pull', 'kcapd/somef']
        # subprocess.run(docker_pull_command, check=True)
        
        # Initialize a list to hold the output for each link
        results = []
        
        # Read the CSV file
        with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                link = row['Link']  # Assuming 'Link' is the column name
                # Construct the Docker run command for each link
                docker_run_command = [
                    'docker', 'run', '--rm', '-v', f'{os.getcwd()}:/data',
                    'kcapd/somef', 
                    'somef', 'describe', 
                    '-r', link, 
                    '-o', '/data/temp_output.json',  # Temporary output file
                    '-t', '0.8'
                ]
                try:
                    subprocess.run(docker_run_command, check=True)
                    # Read the temporary output file and add its content to the results list
                    with open('temp_output.json', 'r', encoding='utf-8') as temp_file:
                        link_output = json.load(temp_file)
                        results.append({link: link_output})
                except subprocess.CalledProcessError as e:
                    print(f"Error processing {link}: {e}")
        
        # Write the results to the output JSON file
        with open(output_json_path, 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)
        
        # Clean up the temporary output file
        os.remove('temp_output.json')

# Write the results to a JSON file
with open(output_json_path, 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=4)


# import csv
# import json
# import subprocess

# # Define the path to the input CSV and output JSON files
# input_csv_path = 'combined_csAI.csv'
# output_json_path = 'extracted_categories.json'

# # Initialize a dictionary to hold the Link and extracted categories
# results = {}

# # Read the CSV file
# with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         link = row['Link']  # Assuming 'Link' is the column name
#         # Run the somef command using Docker
#         try:
#             docker_command = 'docker pull kcapd/somef && docker run -it kcapd/somef /bin/bash somef describe -r ' + link
#             output = subprocess.check_output(
#                 docker_command,
#                 shell=True,
#                 universal_newlines=True
#             )
#             # Here you would parse the output to extract the categories
#             # This is a placeholder as parsing will depend on the somef output format
#             categories = output  # Placeholder for actual parsing logic

#             # Store the results
#             results[link] = categories
#         except subprocess.CalledProcessError as e:
#             print(f"Error processing {link}: {e}")

# # Write the results to a JSON file
# with open(output_json_path, 'w', encoding='utf-8') as json_file:
#     json.dump(results, json_file, ensure_ascii=False, indent=4)