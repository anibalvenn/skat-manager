import csv
from src.controllers.player_controller import PlayerController
from src.controllers.series_controller import SeriesController
import pandas as pd





class ChampionshipController:
    def __init__(self, championship):
        self.championship = championship

    @staticmethod
    def rank_players(csv_path):
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_path)

        # Sort the DataFrame by the "total_points" column in descending order
        df_sorted = df.sort_values(by='total_points', ascending=False)

        # Reset the index of the DataFrame to get the new rank
        df_sorted.reset_index(drop=True, inplace=True)

        # Add the "rank" column to the DataFrame
        df_sorted['rank'] = df_sorted.index + 1

        # Display the player IDs after ranking
        player_ids = df_sorted['player_id']

  
        # Get the number of players in the list
        num_players = len(df_sorted)
        print(f"Number of players in the list: {num_players}")

        # Determine the number of players in the last group
        remaining_players = num_players % 4

        # Build separate arrays based on rankings
        if remaining_players == 0 or remaining_players == 3:
            arrays = [player_ids[i:i+4].tolist() for i in range(0, num_players, 4)]
        elif remaining_players == 1:
            arrays = [player_ids[i:i+4].tolist() for i in range(0, num_players - 9, 4)] +[player_ids[-9:-6].tolist()] +[player_ids[-6:-3].tolist()]+ [player_ids[-3:].tolist()]
        elif remaining_players == 2:
            arrays = [player_ids[i:i+4].tolist() for i in range(0, num_players-6, 4)] +[player_ids[-6:-3].tolist()]+ [player_ids[-3:].tolist()]
      
        # Print the separate arrays
        for i, array in enumerate(arrays, 1):
            print(f"Array {i}: {array.tolist()}")

        # Return the sorted DataFrame with ranks
        return df_sorted

    
csv_path ='C:\\Users\\User\\Documents\\skat\\manager\\playerpoints.csv'

ranked_players = ChampionshipController.rank_players(csv_path)
print(ranked_players)