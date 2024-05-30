import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title('Calculator-GeeksForGeeks')
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()

# Create the entry widget
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)

# Button configuration
button_config = [
    {'text': '1', 'row': 1, 'column': 0}, {'text': '2', 'row': 1, 'column': 1}, {'text': '3', 'row': 1, 'column': 2}, {'text': '+', 'row': 1, 'column': 3},
    {'text': '4', 'row': 2, 'column': 0}, {'text': '5', 'row': 2, 'column': 1}, {'text': '6', 'row': 2, 'column': 2}, {'text': '-', 'row': 2, 'column': 3},
    {'text': '7', 'row': 3, 'column': 0}, {'text': '8', 'row': 3, 'column': 1}, {'text': '9', 'row': 3, 'column': 2}, {'text': '*', 'row': 3, 'column': 3},
    {'text': '0', 'row': 4, 'column': 1}, {'text': '(', 'row': 4, 'column': 0}, {'text': ')', 'row': 4, 'column': 2}, {'text': '/', 'row': 4, 'column': 3},
    {'text': '%', 'row': 5, 'column': 0}, {'text': '**', 'row': 5, 'column': 1}, {'text': '//', 'row': 5, 'column': 2},
    {'text': 'clear', 'row': 5, 'column': 3, 'command': clear},
    {'text': '=', 'row': 6, 'column': 0, 'columnspan': 4, 'command': equal}
]

# Create buttons using a loop
for config in button_config:
    command = config.get('command', lambda text=config['text']: myclick(text))
    button = tk.Button(
        master=frame, text=config['text'], padx=15, pady=5, width=3 if config['text'] not in ['clear', '='] else 9, command=command
    )
    button.grid(row=config['row'], column=config['column'], pady=2, columnspan=config.get('columnspan', 1))

window.mainloop()
