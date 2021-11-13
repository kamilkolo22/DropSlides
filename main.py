import tkinter as tk
from GUI import *


if __name__ == '__main__':
    # Create window
    window = tk.Tk()
    window.title('Tkinter Open File Dialog')

    greeting = tk.Label(text="Wybierz plik pdf oraz miejsce zapisu.", width=50, height=10)
    greeting.pack()

    button_input = tk.Button(text="Select File", width=25, height=5)
    button_input.bind("<Button-1>", ask_for_input)
    button_input.pack()

    button_output = tk.Button(text="Save", width=25, height=5)
    button_output.bind("<Button-1>", ask_for_output)
    button_output.pack()

    button_go = tk.Button(text='RunApp', width=25, height=5)
    button_go.bind("<Button-1>", run_app)
    button_go.pack()

    window.mainloop()

