import pandas as pd
import re

# Function to check if a player is seeded and not containing "Zachary Johnson"
def is_seeded(player):
    return bool(re.search(r'\(\d+\)', player)) and "Zachary Johnson" not in player

# Function to get results against seeded players
def get_results_against_seeded(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Initialize lists to store results
    results_against_seeded = []

    # Iterate over each match
    for index, row in df.iterrows():
        match = row['Match']
        players = match.split(' d. ')
        
        if len(players) == 2:
            player1, player2 = players
            # Check if either player is seeded and does not contain "Zachary Johnson"
            if is_seeded(player1) or is_seeded(player2):
                results_against_seeded.append(row)
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(results_against_seeded)
    return results_df

# Usage
file_path = 'tennis/results.csv'  # Replace with your file path
results_df = get_results_against_seeded(file_path)

# Print the results to the terminal
print(results_df.to_string(index=False))