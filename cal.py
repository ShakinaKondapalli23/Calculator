import tkinter as tk
from tkinter import messagebox
from math import sqrt
from playsound import playsound
import threading

def play_click():
    threading.Thread(target=playsound, args=("click.mp3",), daemon=True).start()

def click(number):
    play_click()
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    play_click()
    entry.delete(0, tk.END)

def backspace():
    play_click()
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    play_click()
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def squareroot():
    play_click()
    try:
        result = sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def show_welcome():
    messagebox.showinfo("Welcome 💖", "Hello, Princess!\nYour Calculator is Ready!")

window = tk.Tk()
window.title("Princess Calculator 💌")
window.geometry("350x470")
window.resizable(False, False)
window.config(bg="#ffe6f0")
window.after(500, show_welcome)

label = tk.Label(window, text="💗 Princess Calculator 💗",
                 font=("Lucida Handwriting", 16, "bold"),
                 bg="#ffe6f0", fg="#a052a0")
label.grid(row=0, column=0, columnspan=4, pady=(10, 0))

entry = tk.Entry(window, font=("Lucida Handwriting", 18, "bold"),
                 width=16, bd=5, relief=tk.GROOVE,
                 bg="#fff0f5", fg="#8e44ad", justify='right')
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10, ipady=8)

buttons = [
    ('7', 2, 0, "#f8c8dc"), ('8', 2, 1, "#f8c8dc"), ('9', 2, 2, "#f8c8dc"), ('/', 2, 3, "#e09fbc"),
    ('4', 3, 0, "#f8c8dc"), ('5', 3, 1, "#f8c8dc"), ('6', 3, 2, "#f8c8dc"), ('*', 3, 3, "#e09fbc"),
    ('1', 4, 0, "#f8c8dc"), ('2', 4, 1, "#f8c8dc"), ('3', 4, 2, "#f8c8dc"), ('-', 4, 3, "#e09fbc"),
    ('0', 5, 0, "#f8c8dc"), ('.', 5, 1, "#f8c8dc"), ('%', 5, 2, "#f4a7b9"), ('+', 5, 3, "#e09fbc"),
    ('C', 6, 0, "#ffc2d1"), ('⌫', 6, 1, "#f4a7b9"), ('√', 6, 2, "#d291bc"), ('=', 6, 3, "#bc8fcd")
]

for (text, row, col, color) in buttons:
    if text == 'C':
        action = clear
    elif text == '⌫':
        action = backspace
    elif text == '=':
        action = calculate
    elif text == '√':
        action = squareroot
    else:
        action = lambda x=text: click(x)

    btn = tk.Button(window,
                    text=text,
                    font=('Lucida Handwriting', 13, 'bold'),
                    bg=color,
                    fg="#6a0572",
                    width=4,
                    height=1,
                    bd=5,
                    relief=tk.RIDGE,
                    activebackground="#ffd6e0",
                    activeforeground="#6a0572",
                    highlightbackground="#fff0f5",
                    highlightthickness=2,
                    command=action)
    btn.grid(row=row, column=col, padx=5, pady=5, ipadx=3, ipady=3)

    btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#ffe0f0"))
    btn.bind("<Leave>", lambda e, b=btn, c=color: b.config(bg=c))

window.mainloop()
