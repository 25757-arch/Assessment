#docstring- Melody Wang- gpu database application
#imports
import sqlite3

# constants and variables
DATABASE = "GPUS.db"

'''functions'''
#print all the gpu nicely
def print_all_gpu():
    db = sqlite3.connect(DATABASE) #connect to sqlite3 database
    