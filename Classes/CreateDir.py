from datetime import date
from datetime import datetime
from pathlib import Path
import os
import subprocess


class CreateDir:

    def __init__(self, name):
        self.name = name
        self.date = datetime.now()
        self.year = self.date.strftime("%Y")
        
        self.str_dir_month = f'{self.name.upper()}_{self.date.strftime("%B")}'
        self.str_dir_year = f'{self.name.upper()}_{self.year}'

    def m_dir(self):

        dir_path = Path(f'logs/{self.str_dir_year}/{self.str_dir_month}')
        
        try:
            dir_path.mkdir(parents=True, exist_ok=True)

        except Exception as e:
            print(f'Error : {e}')


    def makedir(self):
        
        dir_path = Path(f'logs/{self.str_dir_year}')

        try:
            dir_path.mkdir(parents=True, exist_ok=True)

        except Exception as e:
            print(f'Error : {e}')
    
    def makelog(self):

        dir_path = Path(f'logs')

        dir_path.mkdir(parents=True, exist_ok=True)


    def make_all(self):

        self.makelog()
        self.makedir()
        self.m_dir()





