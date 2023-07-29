import sqlite3

class ChampionshipModel:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS championship (
                playerID INTEGER NOT NULL,
                s1 INTEGER DEFAULT 0,
                s2 INTEGER DEFAULT 0,
                s3 INTEGER DEFAULT 0,
                s4 INTEGER DEFAULT 0,
                s5 INTEGER DEFAULT 0,
                s6 INTEGER DEFAULT 0,
                s7 INTEGER DEFAULT 0,
                s8 INTEGER DEFAULT 0,
                s9 INTEGER DEFAULT 0,
                total INTEGER DEFAULT 0,
                FOREIGN KEY (playerID) REFERENCES players(playerID),
                PRIMARY KEY (playerID)
            )
        ''')
        self.conn.commit()

    def insertPlayerPoints(self, seriesLabel, playerID, playerPoints):
        cursor = self.conn.cursor()

        # Update the specified series with the player's points
        cursor.execute(f'UPDATE championship SET {seriesLabel}=? WHERE playerID=?', (playerPoints, playerID))

        # Recalculate the total points for the player by summing all the series points
        cursor.execute('SELECT s1, s2, s3, s4, s5, s6, s7, s8, s9 FROM championship WHERE playerID=?', (playerID,))
        series_points = cursor.fetchone()
        total_points = sum(series_points)
        cursor.execute('UPDATE championship SET total=? WHERE playerID=?', (total_points, playerID))

        self.conn.commit()

    def close_connection(self):
        self.conn.close()
