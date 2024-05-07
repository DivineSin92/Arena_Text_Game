import sqlite3

class Save():
    def __init__(self):
        pass

    def create_table():
        with sqlite3.connect('save.db') as conn:
            sql_create_table = '''CREATE TABLE IF NOT EXISTS saves (
                id integer PRIMARY KEY,
                name text NOT NULL,
                clas text NOT NULL,
                hp int NOT NULL,
                maxhp int NOT NULL,
                dmg int NOT NULL,
                gold int NOT NULL,
                lvl int NOT NULL,
                exp int NOT NULL,
                max_exp int NOT NULL,
                potki int NOT NULL
            )'''
            c = conn.cursor()
            c.execute(sql_create_table)
            print('Table created')

    def create_character(self, name):
        with sqlite3.connect('save.db') as conn:
            Save.checking_character_name_existing(name)
            sql_create_character = 'INSERT INTO saves(name, clas, hp, maxhp, dmg, gold, lvl, exp, max_exp, potki) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            c = conn.cursor()
            c.execute(sql_create_character, (name, self.name, self.hp, self.maxhp, self.dmg, self.gold, self.lvl, self.exp, self.max_exp, self.potki))
            print('character added succesfully')
            
    def check_character():
        with sqlite3.connect('save.db') as conn:
            sql_check_character = 'SELECT * FROM saves'
            c = conn.cursor()
            c.execute(sql_check_character)
            rows = c.fetchall()
            for row in rows:
                print(f'ID: {row[0]}\nName: {row[1]}\nClass: {row[2]}\nhp: {row[3]}\nmahhp: {row[4]}\ndmg: {row[5]}\ngold: {row[6]}\nlvl: {row[7]}\nexp: {row[8]}\npotki: {row[10]}')

    def save_progress(self, name):
        with sqlite3.connect('save.db') as conn:
            sql_save_progress = '''UPDATE saves
            SET clas = ?,
            hp = ?,
            maxhp = ?,
            dmg = ?,
            gold = ?,
            lvl = ?,
            exp = ?,
            max_exp = ?,
            potki = ?
            WHERE name=?'''
            c = conn.cursor()
            c.execute(sql_save_progress, (self.name, self.hp, self.maxhp, self.dmg, self.gold, self.lvl, self.exp, self.max_exp, self.potki, name))
            conn.commit()

    def checking_character_name_existing(name):
        with sqlite3.connect('save.db') as conn:
            sql_checking_character_name_existing = '''DELETE FROM saves WHERE name = ?'''
            c = conn.cursor()
            c.execute(sql_checking_character_name_existing, (name,))
    
    def loading_character(self, name):
        with sqlite3.connect('save.db') as conn:
            sql_loading_character = '''SELECT * FROM saves WHERE name = ?'''
            c = conn.cursor()
            c.execute(sql_loading_character, (name,))
            rows = c.fetchall()
            for row in rows:
                self.name = row[2]
                self.hp = row[3]
                self.maxhp = row[4]
                self.dmg = row[5]
                self.gold = row[6]
                self.lvl = row[7]
                self.exp = row[8]
                self.max_exp = row[9]
                self.potki = row[10]
            Save.save_progress(self, name)