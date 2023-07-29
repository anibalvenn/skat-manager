import sqlite3

class TableModel:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tische (
                tischID INTEGER PRIMARY KEY AUTOINCREMENT,
                posA INTEGER NOT NULL,
                posB INTEGER NOT NULL,
                posC INTEGER NOT NULL,
                posD INTEGER NOT NULL,
                seriesID INTEGER NOT NULL,
                FOREIGN KEY (posA) REFERENCES players(playerID),
                FOREIGN KEY (posB) REFERENCES players(playerID),
                FOREIGN KEY (posC) REFERENCES players(playerID),
                FOREIGN KEY (posD) REFERENCES players(playerID),
                FOREIGN KEY (seriesID) REFERENCES series(seriesID)
            )
        ''')
        self.conn.commit()

    def insertTisch(self, posA, posB, posC, posD, seriesID):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO tische (posA, posB, posC, posD, seriesID) VALUES (?, ?, ?, ?, ?)
        ''', (posA, posB, posC, posD, seriesID))
        self.conn.commit()
        return cursor.lastrowid

    def updateTisch(self, tischID, posA, posB, posC, posD, seriesID):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE tische SET posA=?, posB=?, posC=?, posD=?, seriesID=? WHERE tischID=?
        ''', (posA, posB, posC, posD, seriesID, tischID))
        self.conn.commit()

    def deleteTisch(self, tischID):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM tische WHERE tischID=?', (tischID,))
        self.conn.commit()

    def getAllTische(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM tische')
        return cursor.fetchall()

    def getSeriesTische(self, seriesID):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM tische WHERE seriesID=?', (seriesID,))
        return cursor.fetchall()

    def getSingleTisch(self, tischID):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM tische WHERE tischID=?', (tischID,))
        return cursor.fetchone()

    def close_connection(self):
        self.conn.close()