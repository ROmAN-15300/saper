import tkinter as tk
import random
from tkinter import messagebox


class Minesweeper:
    def __init__(self, master, rows=15, cols=15, mines=30):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = {}
        self.board = []
        self.game_over_button = None  # Кнопка "Начать с начала"
        self.game_over_flag = False  # Флаг для отслеживания состояния игры

        # Устанавливаем фиксированный размер окна
        self.window_width = 800
        self.window_height = 800
        self.cell_width = self.window_width // self.cols
        self.cell_height = self.window_height // self.rows

        # Конфигурация окна
        self.master.geometry(f"{self.window_width}x{self.window_height}")
        self.master.title("Сапёр")

        self.create_widgets()
        self.create_board()
        self.place_mines()
        self.calculate_numbers()

    def create_widgets(self):
        # Создание кнопок для игрового поля
        for r in range(self.rows):
            for c in range(self.cols):
                button = tk.Button(
                    self.master,
                    width=self.cell_width // 10,
                    height=self.cell_height // 20,
                    font=("Arial", self.cell_width // 5),
                    command=lambda r=r, c=c: self.reveal_cell(r, c)
                )
                button.bind("<Button-3>", lambda e, r=r, c=c: self.flag_cell(r, c))  # Обработчик для флага
                button.place(x=c * self.cell_width, y=r * self.cell_height, width=self.cell_width, height=self.cell_height)
                self.buttons[(r, c)] = button

        # Кнопка для перезапуска игры, скрытая по умолчанию
        self.game_over_button = tk.Button(
            self.master,
            text="🔄",
            font=("Arial", 20),
            command=self.restart_game,
            bg="lightgray",
            bd=2
        )
        # Скрываем кнопку перезагрузки при запуске
        self.game_over_button.place_forget()

    def create_board(self):
        # Создание пустой доски
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def place_mines(self):
        # Размещение мин на доске
        count = 0
        while count < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if self.board[r][c] == 0:
                self.board[r][c] = -1
                count += 1

    def calculate_numbers(self):
        # Подсчет чисел вокруг мин
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    continue
                self.board[r][c] = sum(
                    self.board[nr][nc] == -1
                    for nr in range(r - 1, r + 2)
                    for nc in range(c - 1, c + 2)
                    if 0 <= nr < self.rows and 0 <= nc < self.cols
                )

    def reveal_cell(self, r, c):
        # Открытие ячейки при клике
        if self.game_over_flag:  # Проверяем, не закончена ли игра
            return

        if self.board[r][c] == -1:
            self.buttons[(r, c)].config(text="💣", bg="red", font=("Arial", self.cell_width // 5))
            self.game_over()
        elif self.board[r][c] > 0:
            self.buttons[(r, c)].config(
                text=str(self.board[r][c]),
                state="disabled",
                bg="#d3d3d3",
                font=("Arial", self.cell_width // 5)
            )
        else:
            self.buttons[(r, c)].config(state="disabled", bg="#d3d3d3")
            for nr in range(r - 1, r + 2):
                for nc in range(c - 1, c + 2):
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and self.buttons[(nr, nc)]["state"] != "disabled":
                        self.reveal_cell(nr, nc)

    def flag_cell(self, r, c):
        # Установка флага на ячейке
        current_text = self.buttons[(r, c)].cget("text")
        if current_text == "":
            self.buttons[(r, c)].config(text="🚩", fg="red", font=("Arial", self.cell_width // 5))
        elif current_text == "🚩":
            self.buttons[(r, c)].config(text="")

    def game_over(self):
        # Функция, вызываемая при проигрыше
        self.game_over_flag = True  # Игра окончена
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    self.buttons[(r, c)].config(text="💣", bg="red", font=("Arial", self.cell_width // 5))
        messagebox.showinfo("Game Over", "Вы проиграли!")
        # Показываем кнопку в центре экрана
        self.game_over_button.place(relx=0.5, rely=0.5, anchor="center")

    def restart_game(self):
        # Сброс состояния игры
        self.game_over_flag = False
        for button in self.buttons.values():
            button.config(text="", state="normal", bg="SystemButtonFace")
        self.board = []
        self.create_board()
        self.place_mines()
        self.calculate_numbers()
        self.game_over_button.place_forget()  # Скрываем кнопку перезапуска после старта новой игры
