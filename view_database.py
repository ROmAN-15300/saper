import sqlite3


# Функция для отображения истории игр из базы данных
def show_game_history():
    conn = sqlite3.connect('game_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM games")
    games = cursor.fetchall()

    print("История игр:")
    for game in games:
        print(f"ID: {game[0]}, Время начала: {game[1]}, Уровень: {game[2]}")

    conn.close()


# Вызов функции для вывода данных
show_game_history()
