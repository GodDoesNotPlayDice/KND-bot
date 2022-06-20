import sqlite3 as sql3
from functions.functions import Frase
import time
conexion = sql3.connect('database.db')
cursor = conexion.cursor()
sql = """ 
    id_frase INTEGER PRIMARY KEY AUTOINCREMENT,
    frase varchar(225) NOT NULL,
    descripcion varchar(225),
    author int(25) NOT NULL,
    fecha date NOT NULL,
);
"""
frase = 'Hola mundo'
desc = 'Descripcion'
id = 289880246650535937
date = time.localtime()
frase = Frase(frase,desc,id,date)
cursor.execute(f"INSERT INTO FRASE VALUES(null, {frase.getFrase()}, {frase.getFrase()}, {frase.getDesc()}, {frase.getAuthor()}, {frase.getDate()});")
cursor.execute("SELECT titulo FROM FRASE;")
producto = cursor.fetchone()
print(producto)


