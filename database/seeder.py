import sqlite3 as sql

DB_PATH = "C:\\Users\\DanielBayerri\\Desktop\\Salou\\Salou\\database\\salou.db"

def create_database():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE consultes (
        numero integer,
        doctor text,
        llista text
        )""")
    conn.commit()
    conn.close()

def add_database():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (26, "Yolanda Ortega", "vendes"),
        (29, "Jordi Daniel", "vetadine, coliri"),
        (431, "Jesus", "vetadine, coliri, gasses")
    ]
    cursor.executemany("""INSERT INTO consultes VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    create_database()
    add_database()

