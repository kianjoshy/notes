from .CreateFile import CreateFile
from .CreateDir import CreateDir


from datetime import date
from datetime import datetime
from pathlib import Path
import os
import subprocess
import tkinter as tk



class Gui:

    def __init__(self, name, location = ''):
        self.name = name
        self.location = location
        
        self.date = datetime.now()
        self.date_dmy = self.date.strftime("%d%b%Y")

        #empty variables 
        self.input = ''

        #GUI
        self.root = tk.Tk()
        self.root.title(f'{self.name}')
        self.root.geometry("300x200")

        #widgets
        self.entry_box = tk.Entry(self.root, width=30)
        self.entry_box.pack(pady=10)

        self.button = tk.Button(self.root, text="Submit", command=self.on_button_click)
        self.button.pack(pady=10)


    def get_input(self):
        self.input = entry_box.get()



    def on_button_click(self):
        input = self.entry_box.get()
        create_dir = CreateDir(input)
        create_file = CreateFile(input,'txt')
        
        create_dir.make_all()
        create_file.makefile()

    def run_gui(self):
        
        self.root.mainloop()


    
