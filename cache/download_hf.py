from datasets import load_dataset

# Load a dataset and specify a cache directory
dataset = load_dataset('osunlp/TravelPlanner','validation')['validation']

# Select specific rows by their indices (e.g., the first 100 rows)
selected_dataset = dataset.select([11, 38, 50])

# Save the selected rows to a CSV file
selected_dataset.to_csv('cache/selected_validation.csv')
