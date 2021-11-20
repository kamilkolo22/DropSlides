from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from FindAndDelete import *


class ButtonMethods:
    """Class that wraps all methods bind with buttons"""
    def __init__(self):
        self.input = None
        self.output = None

    def ask_for_input(self, event):
        filetypes = (
            ('PDF files', '*.pdf'),
            ('All files', '*.*')
        )
        self.input = askopenfilenames(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

    def ask_for_output(self, event):
        self.output = askdirectory()

    def run_app(self, event):
        if self.input is None:
            showerror("Błąd", "Nie wybrano pliku!")
            return 0
        for input in self.input:
            output = self.set_default_path(input)
            try:
                delete_slides(input, output)
                showinfo("Sukces!", f'Plik został zapisany w {output}')
            except Exception as e:
                showerror("Błąd!", f'Tworzenie nowego pliku nie powiodło się: {e}')
        self.output = None
        self.input = None

    def set_default_path(self, input):
        # Default path
        if self.output is None or self.output == '':
            return f'{input[:-4]}_short.pdf'
        else:
            return self.output + f'/{os.path.basename(input)[:-4]}_short.pdf'
