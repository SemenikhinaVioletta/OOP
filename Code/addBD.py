# This Python code snippet is connecting to a SQLite database named "Pc.db" located in the "BaseDate" directory. It then performs the following operations:
import sqlite3 as bd

conn = bd.connect("BaseDate\Pc.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM Status_klient")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('''
               INSERT INTO Status_klient (Id_status_klient, Name_status_klient) VALUES(?, ?)
               ''', (4, 'Sad'))
conn.commit()