import pandas as pd
import re

# Load the data from the CSV file
def load_data(filename):
    return pd.read_csv(filename)

# Display all matches for a specific tournament
def display_tournament_matches(data, tournament_name):
    tournament_matches = data[data['Tournament'].str.contains(tournament_name, case=False, na=False)]
    return tournament_matches

# Display all matches for a specific player
def display_player_matches(data, player_name):
    player_matches = data[data['Match'].str.contains(player_name, case=False, na=False)]
    return player_matches

# Display all wins for a specific player
def display_player_wins(data, player_name):
    wins = data[(data['Match'].str.contains(player_name, case=False, na=False)) & 
                (data['Match'].str.contains(f"{player_name} d.", case=False, na=False))]
    return wins

# Display all losses for a specific player
def display_player_losses(data, player_name):
    losses = data[(data['Match'].str.contains(player_name, case=False, na=False)) & 
                  (~data['Match'].str.contains(f"{player_name} d.", case=False, na=False))]
    return losses

# Display all matches for a specific round
def display_round_matches(data, round_name):
    round_matches = data[data['Round'].str.contains(round_name, case=False, na=False)]
    return round_matches

# Display the total number of wins and losses for a specific player
def display_player_record(data, player_name):
    wins = display_player_wins(data, player_name)
    losses = display_player_losses(data, player_name)
    return len(wins), len(losses)

# Function to remove seed numbers from player names
def remove_seeds(match):
    return re.sub(r'\(\d+\) ', '', match)

# Function to find repeated opponents
def find_repeated_opponents(data, player_name):
    data['Match'] = data['Match'].apply(remove_seeds)
    player_matches = data[data['Match'].str.contains(player_name, case=False, na=False)]
    opponents = player_matches['Match'].str.extractall(r'\b(?:d\.|d|d.\b)?\s*([A-Za-z ]+)')[0]
    opponents = opponents.str.strip()  # Remove any leading/trailing spaces
    repeated_opponents = opponents.value_counts()[opponents.value_counts() > 1]
    return repeated_opponents

# Function to count sets won and lost at each scoreline
def count_scorelines(data, player_name):
    scorelines = {
        "6-0": 0, "6-1": 0, "6-2": 0, "6-3": 0, "6-4": 0, "7-5": 0, "7-6": 0,
        "8-0": 0, "8-1": 0, "8-2": 0, "8-3": 0, "8-4": 0, "8-5": 0, "8-6": 0, "8-7": 0
    }
    sets_won = scorelines.copy()
    sets_lost = scorelines.copy()
    
    matches = data[data['Match'].str.contains(player_name, case=False, na=False)]
    for index, row in matches.iterrows():
        if pd.notna(row['Score']):
            sets = re.findall(r'\d+-\d+', row['Score'])
            for set_score in sets:
                if set_score in scorelines:
                    if f"{player_name} d." in row['Match']:
                        sets_won[set_score] += 1
                    else:
                        sets_lost[set_score] += 1
    
    return sets_won, sets_lost

# Main function to test the above functions
def main():
    filename = 'tennis/results.csv'
    data = load_data(filename)
    
    # Set pandas display options to show more rows
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    
    # Display all matches for a specific tournament
    tournament_name = "INDIAN WELLS TENNIS GARDEN HOLIDAY JR OPEN"
    print(f"Matches for {tournament_name}:")
    print(display_tournament_matches(data, tournament_name))
    
    # Display all matches for a specific player
    player_name = "Zachary Johnson"
    print(f"\nMatches for {player_name}:")
    player_matches = display_player_matches(data, player_name)
    print(player_matches)
    print(f"\nTotal matches for {player_name}: {len(player_matches)}")
    
    # Display all wins for a specific player
    print(f"\nWins for {player_name}:")
    print(display_player_wins(data, player_name))
    
    # Display all losses for a specific player
    print(f"\nLosses for {player_name}:")
    print(display_player_losses(data, player_name))
    
    # Display the total number of wins and losses for a specific player
    wins, losses = display_player_record(data, player_name)
    print(f"\nRecord for {player_name}: {wins} Wins, {losses} Losses")
    
    # Display repeated opponents for a specific player
    print(f"\nRepeated opponents for {player_name}:")
    print(find_repeated_opponents(data, player_name))
    
    # Display scorelines won and lost for a specific player
    sets_won, sets_lost = count_scorelines(data, player_name)
    print(f"\nSets won for {player_name}:")
    print(sets_won)
    print(f"\nSets lost for {player_name}:")
    print(sets_lost)

if __name__ == "__main__":
    main()