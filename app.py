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
    print("brand          model          vram      speed     price     ") #add title on the first line
    #print (results) #For the first test, the data was shown in a continuous style disorderly
    # loop through all the results
    for gpu in results:
        #print(gpu) #For the second test, the data is displayed in columns, separated by commas, with parentheses at the beginning and end.
        #print(f"{fighter[1]}{fighter[2]}{fighter[3]}{fighter[4]}{fighter[5]}") #For the third test, the data is displayed in columns, no symbols separate, no parentheses.
        print(f"{gpu[1]:<15}{gpu[2]:<15}{gpu[3]:<10}{gpu[4]:<10}{gpu[5]:<10}") #For the fourth test, I reserved some blank spaces to ensure that the data in each column can be aligned.