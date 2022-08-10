
import psycopg2
from colors import list_of_colors

conn = psycopg2.connect(database = "testdb", user = "postgres", password = "pass123", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()
try:
      cur.execute('''CREATE TABLE T_SHIRT_COLORS
            (ID INT PRIMARY KEY     NOT NULL,
            COLOR           TEXT    NOT NULL,
            FREQUENCY           INT     NOT NULL;''')
except:
      pass

color_name = ['GREEN','YELLOW','BROWN','BLUE','PINK','ORANGE','CREAM', 'RED', 'WHITE', 'ARSH', 'BLACK', 'BLEW']
color_frq = list_of_colors
for i in len(color_name)-1:

      cur.execute(f"INSERT INTO T_SHIRT_COLORS (ID,COLOR,FREQUENCY) \
      VALUES ({i}, {color_name[i]}, {color_frq[i]})");



conn.commit()
conn.close()