

from datetime import date
from datetime import datetime
from pathlib import Path
import os
import subprocess


class CreateFile:


    def __init__(self, name, typ, location=''):
        
        self.type = typ
        self.location = location
        self.name = name
        self.date = datetime.now()
        self.date_dmy = self.date.strftime("%d%b%Y")
        self.date_y = self.date.strftime("%Y")
        self.date_mdyt = self.date.strftime('%a %d %b %Y, %I:%M%p')

        self.str_dir_month = f'{self.name.upper()}_{self.date.strftime("%B")}'
        self.str_dir_year = f'{self.name.upper()}_{self.date_y}'
        self.str_filename = f'{self.date_dmy}.{self.type}'
    
    def makefile(self):
        
        with open(f'logs/{self.str_dir_year}/{self.str_dir_month}/{self.name.lower()}_{self.str_filename}', 'a') as file:

            # appends date at the end
            file.seek(0, os.SEEK_END)
            file.write(f'{self.date_mdyt}\n')
