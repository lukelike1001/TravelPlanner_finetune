import os
import openai
import pandas as pd
from typing import List

# Selects all restaurants in a city given an input CSV
def find_restaurants_by_city(filepath: str ="database/restaurants/scrambled_names_restaurant_2022.csv", city: str ="") -> List[str]:
    restaurants = pd.read_csv(filepath)
    city_restaurants = restaurants[restaurants["City"] == city]
    return city_restaurants

# Finds the cheapest restaurant in a city that meets all possible constraints.
def find_restaurant_with_constraints(
        preferred_cost: float = float("inf"),
        preferred_cuisines: set[str] = {"Chinese", "American", "Italian", "Mexican", "Indian", "Mediterranean", "French"},
        preferred_rating: float = 0.0,
        city: str = ""
    ) -> str:

    # If a valid city was not submitted, reprompt the LLM to identify the city again.
    if city == "":
        print("Please input a valid city to search for restaurants")
        return "Please input a valid city to search for restaurants"

    # Find all restaurants for this city given an input CSV
    selected_restaurants =  find_restaurants_by_city(city=city)

    # Raise an warning message if there are no restaurants in the provided city
    if selected_restaurants.empty:
        print("There are no restaurants in your selected city. Please revise your search.")
        return ""
    
    # Iterate through the selected list of restaurants in the current city.
    for index, row in selected_restaurants.iterrows():
        current_cuisine_tags = set(row["Cuisines"].split(" "))
        if row["Average Cost"] > preferred_cost:
            break
        if row["Aggregate Rating"] >= preferred_rating and current_cuisine_tags.intersection(preferred_cuisines):
            return row["Original Name"]

    # This is a stub function. Implement your logic to find the restaurant.
    print(f"No restaurant matching the provided constraints was found. The cheapest restaurant will be returned as a placeholder.")
    return selected_restaurants.iloc[0]

# Function to extract constraints using GPT-3.5
def extract_constraints() -> dict:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "Extract constraints from natural language queries."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.0,
        n=1,
        stop=None
    )
    constraints = response.choices[0].message['content'].strip()
    return eval(constraints)








if __name__ == "__main__":

    # Load the OpenAI API key from environment variable
    openai_api_key = os.getenv('OPENAI_API_KEY')

    if not openai_api_key:
        raise ValueError("The OPENAI_API_KEY environment variable is not set.")

    # Initialize the OpenAI API with the loaded API key
    openai.api_key = openai_api_key

    # Example natural language query
    query = "Can you find me the cheapest restaurant in the city of Appleton, such that its aggregate rating is above 3.0 and the average cost of a meal is under 40 dollars. Verify that the cuisine is either Mexican or Seafood."
    prompt = f"""\
    You are an assistant that converts natural language queries into constraints for a function. 
    Extract the constraints from the following query and format them as a JSON object with the keys 'preferred_cost', 'preferred_cuisine', 'preferred_rating', and 'city'.
    Cuisines can be identified by the following keywords to look out for:  "Chinese", "American", "Italian", "Mexican", "Indian", "Mediterranean", and "French"

    Query: "{query}"

    Example JSON output format:
    {{
        "preferred_cost": float,
        "preferred_cuisines": {"string"},
        "preferred_rating": float,
        "city": "string"
    }}

    Extracted JSON:
    """

    # Extracted constraints from the query
    constraints = extract_constraints(query)

    # Map extracted constraints to function parameters
    preferred_cost = constraints.get('preferred_cost', float("inf"))
    preferred_cuisines = constraints.get('preferred_cuisines', {"Chinese", "American", "Italian", "Mexican", "Indian", "Mediterranean", "French"})
    preferred_rating = constraints.get('preferred_rating', 0.0)
    city = constraints.get('city', "")

    # Verify that the constraints have been properly extracted
    print(f"""Extracted Constraints:
    - Preferred Cost: {preferred_cost}
    - Preferred Cuisines: {preferred_cuisines}
    - Preferred Rating: {preferred_rating}
    - City: {city}""")

    # Run the function with the extracted parameters
    result = find_restaurant_with_constraints(
        preferred_cost=preferred_cost,
        preferred_cuisines=preferred_cuisines,
        preferred_rating=preferred_rating,
        city=city
    )

    print(f"The cheapest restaurant in {city} is {result}")
