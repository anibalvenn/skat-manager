from src.controllers.series_controller import SeriesController
from src.controllers.player_controller import PlayerController
from src.controllers.table_controller import TableController
from src.entities.championship import Championship
from src.entities.series import Series

file_path = 'C:\\Users\\User\\Documents\\skat\\manager\\samplecsv.csv'
def main():
    # Create the Championship
    num_series = SeriesController.get_number_of_series()
    seriesArr = []
    rawPlayers = PlayerController.create_players_from_csv(file_path)

    # Get the type for each series
    for i in range(1, num_series + 1):
        series_type = SeriesController.get_series_type(i)
        seriesArr.append(series_type)

    # Register players for the championship
    players, rowsByPlayerId = PlayerController.assignRowToPlayers(rawPlayers)
    randomischeSerien = TableController.machAlleRandomischeSerie(rowsByPlayerId, len(seriesArr))
    championship = Championship(len(seriesArr),players,randomischeSerien)
    print(championship)

if __name__ == "__main__":
    main()