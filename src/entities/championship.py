from src.entities.series import Series

class Championship:
    def __init__(self, totalSeriesNum, players, randomischeSerien):
        self.seriesArr = totalSeriesNum
        self.players = players
        self.general_ranking = ''
        self.teams = []
        self.randomischeSerien = randomischeSerien
        self.played_series = 0
        self.current_series = 0
        self.lost_game_value = 0

    