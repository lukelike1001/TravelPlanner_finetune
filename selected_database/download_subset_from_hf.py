"""
download_subset_from_hf.py

tl;dr Download TravelPlanner validation, train, and test datasets from Huggingface.

The Long Version:
Running the entire validation dataset for TravelPlanner takes a lot of time and resources. This file allows you to only select certain rows from the validation dataset (or some other TravelPlanner dataset). I suggest selecting at least one easy, medium, and hard testcase when running tests on your modified TravelPlanner.
"""

from datasets import load_dataset

# Load a dataset and specify a cache directory
dataset = load_dataset('osunlp/TravelPlanner','validation')['validation']

# Select specific rows by their indices (e.g., the first 100 rows)
selected_dataset = dataset.select([11, 38, 50])

# Save the selected rows to a CSV file
selected_dataset.to_csv('cache/selected_validation.csv')
