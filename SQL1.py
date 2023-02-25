from mysql.connector import *
db = connect(host = 'localhost', passwd = '1234', user = 'keshav', database = 'keshav')
cur = db.cursor()

cur.execute('drop table Employee;')  #needed; bcoz we are creating table in code; if it is already their it generate error
cur.execute('create table Employee(Id numeric(2) primary key, EName varchar(45) not null, salary numeric(10,2));')
cur.execute('insert into Employee values(05, "Keshav Banka", 25000),(04, "Pawan Kumar", 18000);')
cur.execute('select* from Employee')        #if a query is printing something we need to fetch it from cursor  
res = cur.fetchall()                        #before reusing it
print(res)      #this statement is not neccessary but we need to fetch 

cur.execute('select ename, id from Employee;')

res = cur.fetchall()
print(res)