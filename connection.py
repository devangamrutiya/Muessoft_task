import sqlite3

try:
    con = sqlite3.connect("MovieData.db")
    print("Database is Created")  
    con.commit()  
except:  
    print("Error is occurred") 
