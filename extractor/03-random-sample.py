import json
import random
import math

def calculate_sample_size(population_size, confidence_level=0.95, margin_of_error=0.05, proportion=0.5):
    # Z-score for 95% confidence level
    Z = 1.96
    # Population size
    N = population_size
    # Margin of error
    E = margin_of_error
    # Proportion
    p = proportion
    
    # Sample size calculation
    numerator = N * Z**2 * p * (1 - p)
    denominator = (N - 1) * E**2 + Z**2 * p * (1 - p)
    sample_size = numerator / denominator
    
    return math.ceil(sample_size)

# Load the JSON file
with open('extractor/02_combined_installation_readmes.json', 'r') as file:
    data = json.load(file)

# Calculate the sample size
population_size = len(data)
sample_size = calculate_sample_size(population_size)

# Function to randomly select a sample of IDs
def select_random_sample(data, sample_size):
    all_ids = list(data.keys())
    sample_ids = random.sample(all_ids, sample_size)
    return sample_ids

# Get the random sample of IDs
sample_ids = select_random_sample(data, sample_size)

# Create a dictionary to store the sample data
sample_data = {sample_id: data[sample_id] for sample_id in sample_ids}

# Save the sample data to a new JSON file
with open('extractor/corpus.json', 'w') as file:
    json.dump(sample_data, file, indent=4)

# Print the selected sample IDs
print(f"Randomly selected sample IDs (Sample size: {sample_size}):")
for sample_id in sample_ids:
    print(sample_id)