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

# Function to log record in 3-set matches
def record_in_three_set_matches(data, player_name):
    three_set_matches = data[data['Score'].str.contains(r'\d+-\d+;\s*\d+-\d+;\s*\d+-\d+', na=False)]
    wins = three_set_matches[three_set_matches['Match'].str.contains(f"{player_name} d.", case=False, na=False)]
    losses = three_set_matches[~three_set_matches['Match'].str.contains(f"{player_name} d.", case=False, na=False)]
    return len(wins), len(losses), wins, losses

# Function to log record in tiebreak sets
def record_in_tiebreaks(data, player_name):
    tiebreak_sets_won = 0
    tiebreak_sets_lost = 0
    tiebreak_win_matches = []
    tiebreak_loss_matches = []

    matches = data[data['Match'].str.contains(player_name, case=False, na=False)]
    for index, row in matches.iterrows():
        if pd.notna(row['Score']):
            sets = re.findall(r'(\d+-\d+)', row['Score'])
            for set_score in sets:
                if set_score == "7-6" and f"{player_name} d." in row['Match']:
                    tiebreak_sets_won += 1
                    tiebreak_win_matches.append(row)
                elif set_score == "6-7" and not f"{player_name} d." in row['Match']:
                    tiebreak_sets_won += 1
                    tiebreak_win_matches.append(row)
                elif set_score == "6-7" and f"{player_name} d." in row['Match']:
                    tiebreak_sets_lost += 1
                    tiebreak_loss_matches.append(row)
                elif set_score == "7-6" and not f"{player_name} d." in row['Match']:
                    tiebreak_sets_lost += 1
                    tiebreak_loss_matches.append(row)
    
    return tiebreak_sets_won, tiebreak_sets_lost, pd.DataFrame(tiebreak_win_matches), pd.DataFrame(tiebreak_loss_matches)

# Function to calculate current streak, longest win streak, and longest losing streak
def calculate_streaks(data, player_name):
    matches = data[data['Match'].str.contains(player_name, case=False, na=False)].iloc[::-1]
    streak = 0
    current_streak = 0
    longest_win_streak = 0
    longest_losing_streak = 0
    current_streak_matches = []
    longest_win_streak_matches = []
    longest_losing_streak_matches = []
    temp_streak_matches = []

    for index, row in matches.iterrows():
        if f"{player_name} d." in row['Match']:
            if streak >= 0:
                streak += 1
                temp_streak_matches.append(row)
            else:
                streak = 1
                temp_streak_matches = [row]
            if streak > longest_win_streak:
                longest_win_streak = streak
                longest_win_streak_matches = temp_streak_matches.copy()
        else:
            if streak <= 0:
                streak -= 1
                temp_streak_matches.append(row)
            else:
                streak = -1
                temp_streak_matches = [row]
            if abs(streak) > longest_losing_streak:
                longest_losing_streak = abs(streak)
                longest_losing_streak_matches = temp_streak_matches.copy()
        current_streak = streak
        current_streak_matches = temp_streak_matches.copy()

    return current_streak, longest_win_streak, abs(longest_losing_streak), current_streak_matches, longest_win_streak_matches, longest_losing_streak_matches


def calculate_total_games(data, player_name):
    games_won = 0
    games_lost = 0

    matches = data[data['Match'].str.contains(player_name, case=False, na=False)]
    for index, row in matches.iterrows():
        if pd.notna(row['Score']):
            sets = re.findall(r'(\d+)-(\d+)', row['Score'])
            for set_score in sets:
                player_games, opponent_games = int(set_score[0]), int(set_score[1])
                if f"{player_name} d." in row['Match']:
                    games_won += player_games
                    games_lost += opponent_games
                else:
                    games_won += opponent_games
                    games_lost += player_games
    
    return games_won, games_lost

# Function to calculate total sets won and lost
def calculate_total_sets(data, player_name):
    sets_won = 0
    sets_lost = 0

    matches = data[data['Match'].str.contains(player_name, case=False, na=False)]
    for index, row in matches.iterrows():
        if pd.notna(row['Score']):
            sets = re.findall(r'(\d+)-(\d+)', row['Score'])
            for set_score in sets:
                player_games, opponent_games = int(set_score[0]), int(set_score[1])
                if f"{player_name} d." in row['Match']:
                    sets_won += 1 if player_games > opponent_games else 0
                    sets_lost += 1 if opponent_games > player_games else 0
                else:
                    sets_won += 1 if opponent_games > player_games else 0
                    sets_lost += 1 if player_games > opponent_games else 0
    
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
    print(f"\n{'='*20} Matches for {tournament_name} {'='*20}")
    print(display_tournament_matches(data, tournament_name))
    print("\n\n")

    # Display all matches for a specific player
    player_name = "Zachary Johnson"
    print(f"\n{'='*20} Matches for {player_name} {'='*20}")
    player_matches = display_player_matches(data, player_name)
    print(player_matches)
    print(f"\nTotal matches for {player_name}: {len(player_matches)}")
    print("\n\n")

    # Display repeated opponents for a specific player
    print(f"\n{'='*20} Repeated opponents for {player_name} {'='*20}")
    print(find_repeated_opponents(data, player_name))
    print("\n\n")

    # Display scorelines won and lost for a specific player
    sets_won, sets_lost = count_scorelines(data, player_name)
    print(f"\n{'='*20} Sets won for {player_name} {'='*20}")
    print(sets_won)
    print("\n\n")
    print(f"\n{'='*20} Sets lost for {player_name} {'='*20}")
    print(sets_lost)
    print("\n\n")

    # Display record in 3-set matches for a specific player
    three_set_wins, three_set_losses, three_set_win_matches, three_set_loss_matches = record_in_three_set_matches(data, player_name)
    print(f"\n{'='*20} 3-set match record for {player_name} {'='*20}")
    print(f"{three_set_wins} Wins, {three_set_losses} Losses")
    print("\n\n")
    print(f"\n{'='*20} 3-set match wins {'='*20}")
    print(three_set_win_matches)
    print("\n\n")
    print(f"\n{'='*20} 3-set match losses {'='*20}")
    print(three_set_loss_matches)
    print("\n\n")

    # Display record in tiebreak sets for a specific player
    tiebreak_sets_won, tiebreak_sets_lost, tiebreak_win_matches, tiebreak_loss_matches = record_in_tiebreaks(data, player_name)
    print(f"\n{'='*20} Tiebreak sets record for {player_name} {'='*20}")
    print(f"{tiebreak_sets_won} Sets Won, {tiebreak_sets_lost} Sets Lost")
    print("\n\n")
    print(f"\n{'='*20} Tiebreak sets won {'='*20}")
    print(tiebreak_win_matches)
    print("\n\n")
    print(f"\n{'='*20} Tiebreak sets lost {'='*20}")
    print(tiebreak_loss_matches)
    print("\n\n")

    # Display current streak, longest win streak, and longest losing streak
    current_streak, longest_win_streak, longest_losing_streak, current_streak_matches, longest_win_streak_matches, longest_losing_streak_matches = calculate_streaks(data, player_name)
    print(f"\n{'='*20} Current streak for {player_name} {'='*20}")
    print(f"{'Win' if current_streak > 0 else 'Loss'} {abs(current_streak)} matches")
    print("Current streak matches:")
    print(pd.DataFrame(current_streak_matches))
    print("\n\n")
    print(f"\n{'='*20} Longest win streak for {player_name} {'='*20}")
    print(f"{longest_win_streak} matches")
    print("Longest win streak matches:")
    print(pd.DataFrame(longest_win_streak_matches))
    print("\n\n")
    print(f"\n{'='*20} Longest losing streak for {player_name} {'='*20}")
    print(f"{longest_losing_streak} matches")
    print("Longest losing streak matches:")
    print(pd.DataFrame(longest_losing_streak_matches))
    print("\n\n")

    # Calculate and display total matches, sets, and games won and lost
    wins, losses = display_player_record(data, player_name)
    sets_won, sets_lost = calculate_total_sets(data, player_name)
    games_won, games_lost = calculate_total_games(data, player_name)
    print(f"\n{'='*20} Total record for {player_name} {'='*20}")
    print(f"Matches Won: {wins}, Matches Lost: {losses}")
    print(f"Sets Won: {sets_won}, Sets Lost: {sets_lost}")
    print(f"Games Won: {games_won}, Games Lost: {games_lost}")
    print("\n\n")

if __name__ == "__main__":
    main()