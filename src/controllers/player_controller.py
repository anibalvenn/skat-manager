import csv
import sys
from src.entities.player import Player

class PlayerController:

    def __init__(self) -> None:
        # Initialize players list to an empty list
        self.players = []

    def get_player_info(self, player_num):
        name = input(f"Enter the name of Player {player_num}: ")
        row = input(f"Enter the row of Player {player_num}: ")
        return name, row
    
    @staticmethod
    def create_players_from_csv( file_path):
        players = []  # Create a local list to store players
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                name = row['name']
                sex = row['sex']
                birth_date = row['birthdate']
                country = row['country']
                playerID = row['player_id']
                player = Player(name, sex, birth_date, country,playerID)
                players.append(player)
        return players  # Return the list of players
    
    @staticmethod
    def assignRowToPlayers( playersArr):
        players = []
        r1=[]
        r2=[]
        r3=[]
        r4=[]
        for i in range(len(playersArr)):
            player = playersArr[i]  
            # Calculate the index based on modulo 4
            index = i % 4

            # Do something based on the value of index
            if index == 0:
                player.row = '1'
                r1.append(player.playerID)
            elif index == 1:
                player.row = '2'               
                r2.append(player.playerID)
            elif index == 2:
                player.row = '3'
                r3.append(player.playerID)
            elif index == 3:
                player.row = '4'
                r4.append(player.playerID)
            
            players.append(player) 
            rowArray = [r1, r2,r3,r4]   
        return players, rowArray  # Return the list of players
