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
    cursor.execute(sql) #execute sql that was just created
    results = cursor.fetchall() #fetch all results
    #print format
    #print (results) #For the first test, the data was shown in a continuous style disorderly
    # loop through all the results
    for gpu in results:
        print(gpu) #For the second test, the data is displayed in columns, separated by commas, with parentheses at the beginning and end.