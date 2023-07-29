from src.entities.tisch import Tisch
from src.entities.series import Series

class TableController:
    def __init__(self) -> None:
        pass
    @staticmethod

    def machAlleRandomischeSerie(groups, num_series):
        num_groups = len(groups)
        num_players_per_group = len(groups[0])

        # Initialize a list to store the tables for each series
        alleSerie = []

        # Create series of tables for each series
        for serieID in range(num_series):
            # Initialize a table for this series
            seriesLabel = serieID +1

            serieTische = []

            # For each player position, pick a player to participate in this table
            for player_position in range(num_players_per_group):

                # Create a new table based on the rotation offset
                table = [groups[group_num][(player_position + group_num*serieID) % num_players_per_group] for group_num in range(num_groups)]
                if (serieID+1) % num_series == 2:
                    table = [table[-1]] + table[:-1]
                if (serieID+1) % num_series == 3:
                    table = table[-2:] + table[:-2]
                if (serieID+1) % num_series == 4:
                    table = table[1:] + table[:1]
                tisch = Tisch(table[0], table[1], table[2], table[3], seriesLabel)
                serieTische.append(tisch)


            # Add the tables for this series to the list of all tables
            meisterschaftSerie = Series(seriesLabel, serieTische)
            alleSerie.append(meisterschaftSerie)

        return alleSerie

# Example usage:
# Suppose we have 4 groups, each with 5 players
# group1 = [1, 2, 3, 4, 5]
# group2 = [6, 7, 8, 9, 10]
# group3 = [11, 12, 13, 14, 15]
# group4 = [16, 17, 18, 19, 20]

# groups = [group1, group2, group3, group4]

# # Generate tables for 5 series
# num_series = 5
# all_series_tables = TableController.machAlleSerie(groups, num_series)

# # Print the tables for each series
# for series, series_tables in enumerate(all_series_tables, 1):
#     print(f"Series {series}:")
#     for i, table in enumerate(series_tables, 1):
#         print(f"Table {i}: {table}")
