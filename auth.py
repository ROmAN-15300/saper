import tkinter as tk
from tkinter import messagebox
import sqlite3
import menu  # Импортируем файл menu.py


# Функция для подключения к базе данных и создания таблицы
def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()


# Функция для регистрации
def register(username, password, root):
    if username == "" or password == "":
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля!")
        return
    try:
        # Проверка на существование пользователя с таким же именем
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=?', (username,))
        user = c.fetchone()
        if user:
            messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует!")
            conn.close()
            return

        # Добавляем пользователя в базу
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        root.destroy()
        menu.show_menu()  # Переходим в меню после успешной регистрации
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


# Функция для входа
def login(username, password, root):
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            messagebox.showinfo("Успех", "Вход выполнен успешно!")
            root.destroy()
            menu.show_menu()  # Переходим в меню после успешного входа
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


# Функция для отображения окна авторизации
def show_auth():
    create_db()  # Создаем базу данных и таблицу, если они ещё не существуют
    auth_window = tk.Tk()
    auth_window.title("Авторизация")
    auth_window.geometry("800x600")  # Устанавливаем размер окна 800x600

    # Вставьте фон, если нужно
    bg_image = tk.PhotoImage(file="background_xp.png")  # Путь к картинке
    bg_label = tk.Label(auth_window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    # Текст и поля для ввода
    tk.Label(auth_window, text="Имя пользователя:", bg="white", fg="black", font=("Arial", 16), relief="solid",
             bd=2).place(relx=0.5, rely=0.3, anchor="center")
    username_entry = tk.Entry(auth_window, font=("Arial", 16), relief="solid", bd=2)
    username_entry.place(relx=0.5, rely=0.37, anchor="center", width=300)

    tk.Label(auth_window, text="Пароль:", bg="white", fg="black", font=("Arial", 16), relief="solid", bd=2).place(
        relx=0.5, rely=0.47, anchor="center")
    password_entry = tk.Entry(auth_window, show="*", font=("Arial", 16), relief="solid", bd=2)
    password_entry.place(relx=0.5, rely=0.54, anchor="center", width=300)

    # Кнопки с отступами
    tk.Button(auth_window, text="Войти", bg="white", font=("Arial", 16), relief="solid", bd=2,
              command=lambda: login(username_entry.get(), password_entry.get(), auth_window)).place(relx=0.5, rely=0.64,
                                                                                                    anchor="center",
                                                                                                    width=200,
                                                                                                    height=50)
    tk.Button(auth_window, text="Зарегистрироваться", bg="white", font=("Arial", 16), relief="solid", bd=2,
              command=lambda: register(username_entry.get(), password_entry.get(), auth_window)).place(relx=0.5,
                                                                                                       rely=0.74,
                                                                                                       anchor="center",
                                                                                                       width=200,
                                                                                                       height=50)

    # Кнопка для показа пользователей
    tk.Button(auth_window, text="Показать пользователей", bg="white", font=("Arial", 16), relief="solid", bd=2,
              command=show_users).place(relx=0.5, rely=0.84, anchor="center", width=250, height=50)

    auth_window.mainloop()


def show_users():
    try:
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT username FROM users')
        users = c.fetchall()
        conn.close()

        user_list = "\n".join([user[0] for user in users])
        messagebox.showinfo("Список пользователей", user_list)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


if __name__ == "__main__":
    show_auth()  # Показываем окно авторизации при запуске программы
