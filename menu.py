import tkinter as tk
from saper import Minesweeper  # Импортируем класс игры

def start_game(rows, cols, mines):
    # Создаем новое окно для игры
    game_window = tk.Tk()
    game_window.title("Сапёр")
    game_window.geometry("800x600")  # Размер окна
    game_window.resizable(False, False)  # Запрещаем изменение размера окна

    # Запускаем игру с переданными параметрами
    Minesweeper(game_window, rows, cols, mines)

def show_menu():
    # Создаем главное окно меню
    menu_window = tk.Tk()
    menu_window.title("Меню игры")
    menu_window.geometry("800x600")  # Размер окна
    menu_window.resizable(False, False)  # Запрещаем изменение размера окна

    # Добавляем фон
    background_image = tk.PhotoImage(file="background_xp.png")  # Путь к изображению фона
    background_label = tk.Label(menu_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # Фиксируем фон на весь экран

    # Заголовок
    title_label = tk.Label(menu_window, text="Сапёр", font=("Arial", 50, "bold"), fg="black")
    title_label.pack(pady=50)  # Отступ между заголовком и кнопками

    # Кнопки для уровней сложности
    button_frame = tk.Frame(menu_window, bg="lightgreen", bd=0)  # Прозрачный контейнер для кнопок
    button_frame.pack(pady=20)  # Пространство вокруг кнопок

    # Кнопки для уровней
    easy_button = tk.Button(button_frame, text="Лёгкий", font=("Arial", 20), width=15, height=2, command=lambda: start_game(15, 15, 30))
    easy_button.grid(row=0, column=0, padx=10, pady=10)

    medium_button = tk.Button(button_frame, text="Средний", font=("Arial", 20), width=15, height=2, command=lambda: start_game(18, 18, 45))
    medium_button.grid(row=1, column=0, padx=10, pady=10)

    hard_button = tk.Button(button_frame, text="Сложный", font=("Arial", 20), width=15, height=2, command=lambda: start_game(21, 21, 60))
    hard_button.grid(row=2, column=0, padx=10, pady=10)

    menu_window.mainloop()

# Запуск меню
if __name__ == "__main__":
    show_menu()
