#docstring- Melody Wang- gpu database application
#imports
import sqlite3

# constants and variables
DATABASE = "GPUS.db"

'''functions'''
#print all the gpu nicely
def print_all_gpu():
    db = sqlite3.connect(DATABASE) #connect to sqlite3 database
    cursor = db.cursor() #build a cursor then have the access to operate the data
    #sql statement
    sql = "SELECT * FROM gpu;" #set an sql query