

from datetime import datetime
from datetime import date
import os


date = datetime.now()

def createfile(name):
   
    date_dmy = date.strftime("%d%b%Y")
    print('this ran')
    with open(f'{str(name)}_{date_dmy}.txt', 'a') as file:
        write_at_end(file)    


def write_at_end(file):

 
    file.seek(0, os.SEEK_END)
    date_mdyt = date.strftime('%a %d %b %Y, %I:%M%p')
    file.write(f'{date_mdyt}\n')

def main():

    createfile('n')


main()
