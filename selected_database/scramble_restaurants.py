import pandas as pd
import random
import string

"""
scramble_restaurants.py

tl;dr Scrambles all TravelPlanner restaurant names into a series of a random chars and numerical digits.

The Long Version:
The TravelPlanner developer team **randomly** assigned cuisine tags (e.g., Chinese, French, Seafood) and price tags (e.g., $67) to all restaurants as downloaded from "clean_restaurants_2022.csv". This can lead to funny situations where McDonald's is labeled as a seafood restaurant, or China Garden is considered a pizzeria.

Let's say we want to plan a 3-day trip from Chicago to New York City that ONLY visit SEAFOOD restaurants. The generated itinerary may suggest visiting the aforementioned McDonald's, which can confuse the prompter. In this case, the LLM is correct... but it looks weird due to the randomized data. Alternatively, the LLM may attribute McDonald's as a fast food restaurant instead of a seafood restaurant (like most humans would). In this case, the LLM shows common sense... but is technically wrong.

To remove any sort of bias and correlation between restaurant names and their cuisine tags, this python file takes in "clean_restaurants_2022.csv" and scrambles all TravelPlanner restaurant names into a series of a random chars and numerical digits. The original name is still kept in a new column to cross-check it with the original csv.

If you need the "clean_restaurants_2022.csv", you can download it from the TravelPlanner team's Google Drive as provided here: https://drive.google.com/file/d/1pF1Sw6pBmq2sFkJvm-LzJOqrmfWoQgxE/view?usp=sharing

"""

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
