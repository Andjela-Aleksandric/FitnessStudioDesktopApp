import sqlite3

conn = sqlite3.connect('fitnes_studio.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS fitnes_studio_baza
          ([id_clana] INTEGER PRIMARY KEY, [ime_clana] TEXT, [tip_clanarine] TEXT, [broj_telefona] TEXT)
          ''')
# c.execute('''
#           INSERT INTO fitnes_studio_baza (id_clana, ime_clana, tip_clanarine, broj_telefona )
#
#                 VALUES
#                 (1,'Aleksandra Perović', 'joga', '+38163272931'),
#                 (2,'Anđela Aleksandrić', 'personalni trening', '+381611866300'),
#                 (3,'Đina Perović', 'pilates', '0113178303')
#           ''')