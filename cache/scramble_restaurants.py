import pandas as pd
import random
import string

# Set the random seed for deterministic output
random.seed(5514)

# Assuming changeName is a pre-built function. Here is the modified implementation.
def changeName(row_number):
    # Generate a random sequence of letters and numbers
    random_sequence = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    # Append the row number to the end
    return f"{random_sequence}_{row_number}"

# Read the CSV file
input_csv = 'database/restaurants/clean_restaurant_2022.csv'
output_csv = 'database/restaurants/scrambled_names_restaurant_2022.csv'
df = pd.read_csv(input_csv)

# Rename one of the unnamed dataframes
df.rename(columns={'Unnamed: 0': ''}, inplace=True)

# Keep a copy of the original name for reference
df['Original Name'] = df['Name']

# Replace the names in the "Name" column with the modified names including the row number
df['Name'] = df.index.to_series().apply(lambda idx: changeName(idx))

# Sort the restaurants in increasing cost
sorted_df = df.sort_values(by='Average Cost')

# Save the modified DataFrame to a new CSV file
sorted_df.to_csv(output_csv, index=False)

print(f"Modified CSV saved as {output_csv}")
