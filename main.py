import tkinter as tk
from GUI import ButtonMethods


if __name__ == '__main__':
    # Create window
    window = tk.Tk()
    window.title('Usuwacz slajdów')

    # Create class that will control source scripts
    BT = ButtonMethods()

    instruction_text = "Wybierz plik pdf oraz miejsce zapisu.\n" + \
                       "Domyślna ścieżka zapisu to ścieżka_pliku+'_short.pdf'"
    instruction = tk.Label(text=instruction_text, width=50, height=5)
    instruction.pack()

    button_input = tk.Button(text="Wybierz plik", width=25, height=5)
    button_input.bind("<Button-1>", lambda e: BT.ask_for_input(e))
    button_input.pack()

    button_output = tk.Button(text="Wybierz miejsce zapisu", width=25, height=5)
    button_output.bind("<Button-1>", lambda e: BT.ask_for_output(e))
    button_output.pack()

    button_go = tk.Button(text='GO!', width=25, height=5)
    button_go.bind("<Button-1>", lambda e: BT.run_app(e))
    button_go.pack()

    bottom_label = tk.Label(text="This app is inspired by Matthew BrotherInLaw", width=50, height=4)
    bottom_label.config(font=("Garamond", 8))
    bottom_label.pack()

    window.mainloop()
