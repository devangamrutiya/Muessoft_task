from connection import *

try: 
    con.execute(
        "create table if not exists movies (id integer primary key autoincrement, name text, actor_name text, actress_name text, year_of_release int,  director_name text)")

    print("Table is Created")  

except:
    print("Table is Not Created")  

con.commit() 
