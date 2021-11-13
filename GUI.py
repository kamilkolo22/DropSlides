from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
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
        self.input = askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

    def ask_for_output(self, event):
        files = [('PDF files', '*.pdf'),
                 ('All files', '*.*')]
        self.output = asksaveasfilename(filetypes=files, defaultextension=files)

    def run_app(self, event):
        if self.output is None or self.output == '':
            self.output = self.set_default_path()
        if self.input is None:
            showerror("Błąd", "Nie wybrano pliku!")
        else:
            try:
                delete_slides(self.input, self.output)
                showinfo("Sukces!", f'Plik został zapisany w {self.output}')
            except Exception as e:
                showerror("Błąd!", f'Tworzenie nowego pliku nie powiodło się: {e}')

    def set_default_path(self):
        # Default path
        return f'{self.input[:-4]}_short.pdf'
