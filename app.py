#docstring- Melody Wang- gpu database application
#imports
import sqlite3

# constants and variables
DATABASE = "GPUS.db"
FORMAT_STR = "{:<15}{:<15}{:<10}{:<10}{:<10}" #set a variable to avoid magic numbers


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
    print("\nPrint all gpu: ") #add title
    print("brand          model          vram      speed     price     ") #add title on the first line
    #print (results) #For the first test, the data was shown in a continuous style disorderly
    # loop through all the results
    for gpu in results:
        #print(gpu) #For the second test, the data is displayed in columns, separated by commas, with parentheses at the beginning and end.
        #print(f"{fighter[1]}{fighter[2]}{fighter[3]}{fighter[4]}{fighter[5]}") #For the third test, the data is displayed in columns, no symbols separate, no parentheses.
        #print(f"{gpu[1]:<15}{gpu[2]:<15}{gpu[3]:<10}{gpu[4]:<10}{gpu[5]:<10}") #For the fourth test, I reserved some blank spaces to ensure that the data in each column can be aligned.
        print(FORMAT_STR.format(gpu[1], gpu[2], gpu[3], gpu[4], gpu[5])) #set a variable to avoid magic numbers
    db.close() #loop finished here

#print all the gpu sorted by vram
def print_all_gpu_by_vram():
    db = sqlite3.connect(DATABASE) #connect to sqlite3 database
    cursor = db.cursor() #build a cursor then have the access to operate the data
    #sql statement
    sql = "SELECT * from gpu ORDER by vram DESC;" #set an sql query
    cursor.execute(sql) #execute sql that was just created
    results = cursor.fetchall() #fetch all results
    #print format
    print("\nPrint all gpu by vram:")
    print("brand          model          vram      speed     price     ") #add title on the first line
    for gpu in results:  
        print(FORMAT_STR.format(gpu[1], gpu[2], gpu[3], gpu[4], gpu[5]))
    db.close() #loop finished here

#print all the gpu sorted by speed
def print_all_gpu_by_speed():
    db = sqlite3.connect(DATABASE) #connect to sqlite3 database
    cursor = db.cursor() #build a cursor then have the access to operate the data
    #sql statement
    sql = "SELECT * from gpu ORDER by speed DESC;" #set an sql query
    cursor.execute(sql) #execute sql that was just created
    results = cursor.fetchall() #fetch all results
    #print format
    print("\nPrint all gpu by speed:")
    print("brand          model          vram      speed     price     ") #add title on the first line
    for gpu in results:  
        print(FORMAT_STR.format(gpu[1], gpu[2], gpu[3], gpu[4], gpu[5]))
    db.close() #loop finished here

#print all the gpu sorted by price
def print_all_gpu_by_price():
    db = sqlite3.connect(DATABASE) #connect to sqlite3 database
    cursor = db.cursor() #build a cursor then have the access to operate the data
    #sql statement
    sql = "SELECT * from gpu ORDER by price DESC;" #set an sql query
    cursor.execute(sql) #execute sql that was just created
    results = cursor.fetchall() #fetch all results
    #print format
    print("\nPrint all gpu by price:")
    print("brand          model          vram      speed     price     ") #add title on the first line
    for gpu in results:  
        print(FORMAT_STR.format(gpu[1], gpu[2], gpu[3], gpu[4], gpu[5]))
    db.close() #loop finished here

#main code
while True:
    user_input = input("\nWhat would you like to do.\n1. Print all gpu.\n2. Print all gpu sorted by vram.\n3. Print all gpu sorted by speed.\n4. Print all gpu sorted by price.\n5. Exit\n")
    if user_input == "1":
        print_all_gpu()
    elif user_input == "2":
        print_all_gpu_by_vram()
    elif user_input == "3":
        print_all_gpu_by_speed()
    elif user_input == "4":
        print_all_gpu_by_price()
    elif user_input == "5":
        break
    else:
        print("That was not an option.")