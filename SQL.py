from mysql.connector import *

db = connect(host = 'localhost', user = 'keshav', passwd = '1234', database = 'keshav') 
#connection established

cur = db.cursor()       #created a cursor in db

#cur.execute('create database keshav;')     #db already created  so it will give error if executed
cur.execute('show databases;')              #new query result stored in cur
res1 = cur.fetchall()                       #result fetched in a new var
print(res1)                    
cur.execute('select * from Student')        #new query
for i in cur:                               #looping through object of cursor i.e. previous query result
    print(i)


#now we can use any number of sql queries and import export data from it