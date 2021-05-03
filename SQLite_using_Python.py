#!/usr/bin/env python
# coding: utf-8

# In[1]:


#creating SQLite Database 
#sqlite 3 is a python inbuilt module to make changes using python
#CREATION OPERATION
#use conn object or cursor object c to execute querries

import sqlite3
conn=sqlite3.connect('3April.db')
c=conn.cursor()
print('opened database successfully')


# In[2]:


#creating a database in SQLite Db
#conn is a connection object
#INSERTION OPERATION

c.execute('''CREATE TABLE COMPANY
         (ID       INT     PRIMARY KEY     NOT NULL,
         NAME      TEXT    NOT NULL,
         AGE       INT     NOT NULL,
         ADDRESS   CHAR(50),
         SALARY    REAL);''')
print ("Table created successfully")


# In[3]:


'''Insetion operation'''

conn.execute('''INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)                VALUES (1, 'Paul', 32, 'California', 20000.00 ) ''')

conn.execute('''INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)                VALUES (2, 'ANUREET', 29, 'California', 70000.00 ) ''')

conn.execute('''INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)                VALUES (3, 'Kanwar', 27, 'India', 90000.00 ) ''')

conn.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)               VALUES (4, 'Teddy', 23, 'Norway', 20000.00 )''');

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)               VALUES (5, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
conn.commit
print('insertion is successful')


# In[7]:


#selection operation 
#using select command
cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3],'\n')

print ("Operation done successfully");


# In[5]:


#update operation
conn.execute('''UPDATE COMPANY set SALARY=10000 WHERE ID=4  ''')
conn.commit
print('updated successfully')


# In[6]:


#delete operation
conn.execute("DELETE from COMPANY where ID = 1;")
conn.commit()
print( "Total number of rows deleted :", conn.total_changes)


# In[8]:


#need to close the connection to reflect insertion or updation of data in the database i.e in sqliteTool one can only see 
# the data only once we close the connection
conn.close()


# In[ ]:




