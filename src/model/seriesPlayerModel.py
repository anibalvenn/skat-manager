import sqlite3

class SeriesPlayerModel:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS series_players (
                playerID INTEGER NOT NULL,
                seriesID INTEGER NOT NULL,
                tischID INTEGER NOT NULL,
                seriesPoints INTEGER,
                lostGames INTEGER,
                dueMoney REAL,
                FOREIGN KEY (playerID) REFERENCES players(playerID),
                FOREIGN KEY (seriesID) REFERENCES series(seriesID),
                FOREIGN KEY (tischID) REFERENCES tische(tischID),
                PRIMARY KEY (playerID, seriesID)
            )
        ''')
        self.conn.commit()

    def insertSeriesPlayer(self, playerID, seriesID, tischID, seriesPoints, lostGames, dueMoney):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO series_players (playerID, seriesID, tischID, seriesPoints, lostGames, dueMoney) VALUES (?, ?, ?, ?, ?, ?)
        ''', (playerID, seriesID, tischID, seriesPoints, lostGames, dueMoney))
        self.conn.commit()

    def updateSeriesPlayer(self, playerID, seriesID, tischID, seriesPoints, lostGames, dueMoney):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE series_players SET tischID=?, seriesPoints=?, lostGames=?, dueMoney=? WHERE playerID=? AND seriesID=?
        ''', (tischID, seriesPoints, lostGames, dueMoney, playerID, seriesID))
        self.conn.commit()

    def deleteSeriesPlayer(self, playerID, seriesID):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM series_players WHERE playerID=? AND seriesID=?', (playerID, seriesID))
        self.conn.commit()

    def getAllSeriesPlayers(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM series_players')
        return cursor.fetchall()

    def getSeriesPlayerByPlayerID(self, playerID):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM series_players WHERE playerID=?', (playerID,))
        return cursor.fetchall()
    
    def getSeriesPlayerByTischID(self, tischID):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM series_players WHERE tischID=?', (tischID,))
        return cursor.fetchall()

    def getSeriesPlayerBySeriesID(self, seriesID):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM series_players WHERE seriesID=?', (seriesID,))
        return cursor.fetchall()

    def close_connection(self):
        self.conn.close()
