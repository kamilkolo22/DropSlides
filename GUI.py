from tkinter import filedialog as fd
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from FindAndDelete import *


def ask_for_input(event):
    global input
    filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
    )
    input = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)


def ask_for_output(event):
    global output
    files = [('PDF files', '*.pdf'),
             ('All files', '*.*')]
    output = asksaveasfilename(filetypes=files, defaultextension=files)

def run_app(event):
    if input is None:
        showerror("Błąd", "Nie wybrano pliku!")
    else:
        try:
            delete_slides(input, output)
            showinfo("Sukces!", f'Plik został zapisany w {output}')
        except NameError:
            delete_slides(input, set_defaults_paths())
            showinfo("Sukces!", f'Plik został zapisany w {set_defaults_paths()}')

def set_defaults_paths():
    # Default path
    # return f'{os.getcwd()}\\pdf_short.pdf'
    return f'{input[:-4]}_short.pdf'
