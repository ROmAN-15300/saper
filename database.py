import sqlite3

# Функция для создания таблицы, если она еще не существует
def create_table():
    conn = sqlite3.connect('game_results.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS game_launches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        level TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()

# Функция для добавления нового запуска игры в базу данных
def insert_game_data(level):
    conn = sqlite3.connect('game_results.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO game_launches (level)
    VALUES (?)
    ''', (level,))

    conn.commit()
    conn.close()

# Функция для получения всех записей из базы данных
def get_game_data():
    conn = sqlite3.connect('game_results.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM game_launches')
    rows = cursor.fetchall()

    conn.close()
    return rows

# Функция для отображения содержимого базы данных в консоли
def show_db_content():
    game_data = get_game_data()
    print(f"Количество запусков игры: {len(game_data)}")

    for data in game_data:
        print(f"ID: {data[0]}, Уровень: {data[1]}, Дата и время: {data[2]}")
