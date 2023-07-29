import sqlite3
from datetime import date

class PlayerModel:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS players (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sex TEXT NOT NULL,
                birthdate TEXT NOT NULL,
                country TEXT NOT NULL,
                row TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_player(self, name, sex, birthdate, country, row):  # Add 'row' as a parameter
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO players (name, sex, birthdate, country, row) VALUES (?, ?, ?, ?, ?)
        ''', (name, sex, birthdate, country, row))
        self.conn.commit()
        return cursor.lastrowid

    def update_player(self, player_id, name, sex, birthdate, country, row):  # Add 'row' as a parameter
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE players SET name=?, sex=?, birthdate=?, country=?, row=? WHERE id=?
        ''', (name, sex, birthdate, country, row, player_id))
        self.conn.commit()

    def delete_player(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM players WHERE id=?', (player_id,))
        self.conn.commit()

    def get_player(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM players WHERE id=?', (player_id,))
        return cursor.fetchone()

    def get_all_players(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM players')
        return cursor.fetchall()
    
    def getPlayerNameByID(self, player_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT name FROM players WHERE id=?', (player_id,))
        player_name = cursor.fetchone()
        return player_name[0] if player_name else None

    def close_connection(self):
        self.conn.close()
