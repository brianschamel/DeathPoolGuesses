
# insertions with SQL 

# importing module 
import sqlite3 
  
# connecting to the database  
connection = sqlite3.connect("DeathPoolGuesses.db") 
  
# cursor  
crsr = connection.cursor() 

# SQL command to create a table in the database 
sql_command = """create table if not exists Guesses (  
CommentID VARCHAR(10) PRIMARY KEY,  
PersonGuessed VARCHAR(20),
DateGuessed DATE,  
commentTimestamp DATETIME,
permalink URL);"""

# execute the statement 
crsr.execute(sql_command) 

connection.commit()
connection.close()
exit
# SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command) 
  
# another SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command) 
  
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
crsr = connection.cursor() 
  
# execute the command to fetch all the data from the table emp 
crsr.execute("SELECT * FROM emp")  
  
# store all the fetched data in the ans variable 
ans= crsr.fetchall()  
  
# loop to print all the data 
for i in ans: 
    print(i) 
# close the connection 
connection.close() 