#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
conn=sqlite3.connect('3April.db')
c=conn.cursor()
print('opened database successfully')

c = conn.execute("SELECT id, name, address, salary from COMPANY")
with open('DB1.txt', 'w') as f:
    for row in c:
        f.write(str(row))  #the argument of this command must be a string not a tuple
        f.write('\n')
    f.close()
print('writing done successfully')

with open('DB1.txt') as f:
    content=f.read()
    print(content)
    f.close()

print('file successfully closed')


# In[ ]:




