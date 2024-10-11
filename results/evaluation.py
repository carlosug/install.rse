"""script for descriptive analysis of annotated repositories with golden data (out sample from bidir.txt dataset)
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data/golden/repo_manual_annotation.csv'  # Dataset for the golden annotations
data = pd.read_csv(file_path)

# Convert 'Star' column to numeric, removing commas
data['Star'] = data['Star'].replace({',': ''}, regex=True).astype(float)

# Calculate the proportion of repositories with installation instructions
installation_counts = data['has_installation'].value_counts(normalize=True)

# Calculate the frequency of headers (h1 to h6)
header_columns = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
header_frequencies = data[header_columns].apply(pd.Series.value_counts).fillna(0).astype(int)

# Calculate the frequency of method types
method_type_frequencies = data['method_type'].value_counts()

# Count the number of installation methods per repository
data['method_count'] = data['method_type'].apply(lambda x: len(x.split(', ')) if pd.notnull(x) else 0)

# Count the frequency of repositories based on the number of installation methods
method_count_distribution = data['method_count'].value_counts().sort_index()

# Create figures and tables

# Create the first figure for Installation Proportions
plt.figure(figsize=(8, 5))
installation_proportions = installation_counts * 100  # Convert to percentages
plt.bar(installation_proportions.index.astype(str), installation_proportions, color=['lightblue', 'salmon'])
plt.title('Proportion of Repositories with Installation Instructions')
plt.xlabel('Has Installation Instructions')
plt.ylabel('Percentage (%)')
plt.xticks(rotation=0)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
installation_proportion_path = 'visualisations/golden/installation_proportion_figure.png'  # Save path for the figure
plt.savefig(installation_proportion_path, bbox_inches='tight')
plt.close()

# Create the second figure for Method Types Distribution
plt.figure(figsize=(8, 5))
method_type_frequencies.plot(kind='bar', color='lightgreen')
plt.title('Distribution of Installation Method Types')
plt.xlabel('Installation Method Type')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.ylim(0, method_type_frequencies.max() + 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
method_types_distribution_path = 'visualisations/golden/method_type_distribution.png'  # Save path for the figure
plt.savefig(method_types_distribution_path, bbox_inches='tight')
plt.close()

# Create a summary table for the distribution of installation method counts
method_count_distribution_table = method_count_distribution.reset_index()
method_count_distribution_table.columns = ['Number of Installation Methods', 'Number of Repositories']

# Create a figure for the distribution of installation method counts
plt.figure(figsize=(8, 5))
plt.bar(method_count_distribution_table['Number of Installation Methods'].astype(str), 
        method_count_distribution_table['Number of Repositories'], color='lightcoral')
plt.title('Distribution of Repositories by Number of Installation Methods')
plt.xlabel('Number of Installation Methods')
plt.ylabel('Number of Repositories')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
installation_method_count_path = 'visualisations/golden/installation_method_count_distribution.png'  # Save path for the figure
plt.savefig(installation_method_count_path, bbox_inches='tight')
plt.close()

# Scatter Plot between Star and number of methods found
# Prepare data for the scatter plot
scatter_data = data[['Star', 'method_count']].drop_duplicates()

# Remove rows with NaN values in 'Star' or 'method_count' columns
scatter_data = scatter_data.dropna(subset=['Star', 'method_count'])

# Create the scatter plot with custom colors
plt.figure(figsize=(8, 5))
plt.scatter(scatter_data['Star'], scatter_data['method_count'], c=scatter_data['Star'], cmap='viridis', alpha=0.6)
plt.colorbar(label='Number of Stars')  # Add a color bar to show the color scale
plt.title('Scatter Plot of Star vs Number of Installation Methods')
plt.xlabel('Number of Stars')
plt.ylabel('Number of Installation Methods')
plt.grid(True, linestyle='--', alpha=0.7)

# Save the scatter plot
scatter_plot_path = 'visualisations/golden/scatter_star_vs_methods.png'  # Save path for the figure
plt.savefig(scatter_plot_path, bbox_inches='tight')
plt.close()

# Output the summary table
print(method_count_distribution_table)