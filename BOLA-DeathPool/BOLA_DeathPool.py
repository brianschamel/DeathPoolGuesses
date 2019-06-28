
#!/usr/bin/python
import praw
import os
import pdb
import re
import sqlite3

connection = sqlite3.connect("DeathPoolGuesses.db") 
  
# cursor  
crsr = connection.cursor() 

# SQL command to create a table in the database 
sql_command = """create table if not exists DeathPoolGuessesTable (  
CommentID VARCHAR(10) PRIMARY KEY,  
PersonGuessed VARCHAR(20),
DateGuessed DATE,  
commentTimestamp DATETIME,
permalink URL);"""

# execute the statement 
crsr.execute(sql_command) 

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("bestoflegaladvice")

if not os.path.isfile("posts_found.txt"):
    posts_found = []
else:
    with open("posts_found.txt", "r") as f:
       posts_found = f.read()
       posts_found = posts_found.split("\n")
       posts_found = list(filter(None, posts_found))

for submission in subreddit.hot(limit=2):
    if (submission.author == "eeech") and ("Death Pool" in submission.title):
        print("Title: ", submission.title)
        print("Author: ", submission.author)
        print("URL: ", submission.url)
        print("---------------------------------\n")
        deathPoolPostID = submission.id

submission = reddit.submission(deathPoolPostID)
submission.comments.replace_more(limit=0)
for top_level_comment in submission.comments:
    print(top_level_comment.body)
    print("---------------------------------\n")
    print("----------------------")

