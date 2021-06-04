#!/usr/bin/env python
# coding: utf-8

# In[18]:


''' Creating a connection with sqlite Db using 
    Python provides two popular interfaces for
    working with the SQLite database library: PySQLite and APSW.
    We will be using PySqlite interface'''
import sqlite3
from sqlite3 import Error

'''First, create a Connection object using the connect() function of the sqlite3 module.'''
def create_connection(db):
    conn=None;
    try:
        conn=sqlite3.connect(db)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            return conn


# In[2]:


'''Second, create a Cursor object by calling the cursor() method of the Connection object.
   Third, pass the CREATE TABLE statement to the execute() method of the Cursor object and execute this method.'''
def create_table(table,conn):
    try:
        cur=conn.cursor()
        cur.execute(table)
    except Error as e:
        print(e)

    


# In[3]:


def main():
    database="C:/sqlite/pythonSqlite.db"
    table1='''Create table If NOT EXISTS projects(
            id integer PRIMARY KEY,
            name text NOT NULL,
            begin_date text,
            end_date text);'''
    table2="""CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
    conn=create_connection(database)
    if conn is not None:
        create_table(table1,conn)
        create_table(table2,conn)
    else: 
        print("error cant complete the connection")
        

main()
    


# In[8]:


'''Third, execute an INSERT statement. If you want to pass arguments to the INSERT statement,
   you use the question mark (?) as the placeholder for each argument.'''

def create_project(conn,task):
    sql=""" insert into projects(name,begin_date,end_date)
            values(?,?,?)"""
    curr=conn.cursor()
    curr.execute(sql,task)
    conn.commit()
    return curr.lastrowid

def create_task(conn,task):
    sql=""" INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?)"""
    curr=conn.cursor()
    curr.execute(sql,task)
    conn.commit()
    return curr.lastrowid


# In[9]:


def main():
    database = "C:\sqlite\pythonSqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        project_id = create_project(conn, project)

        # tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)


    
main()


# In[19]:


def update_task(conn, task):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


# In[32]:


def delete_task(conn, id):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, id)
    conn.commit()


# In[33]:


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)


# In[35]:


def main():
    database = "C:\sqlite\pythonSqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        what= input('u if want to upadate, d if want to delete, i to insert, s to fetch whole data')
        if what=='u':
            update_task(conn, (int(input('enter the priority')), input('enter start date'), input('enter the end date'),int(input('where id is '))))
        elif what=='i':
                    # create a new project
            project = (input('project name'), input('start date'), input('end date'));
            project_id = create_project(conn, project)
        # tasks
            task_1 = (input('name the task'), int(input('priority')), int(input('status id')), project_id, input('begin date'), input('end date'))
            task_2 = ('Confirm with user about the top requirements', 1, 1, project_id,'00-00-00','00-00-00')

        # create tasks
            create_task(conn, task_1)
            create_task(conn, task_2)
        elif what=='d':
            delete_task(conn,int(input('enter the id')))
        else:
            select_all_tasks(conn)
            
            
main()


# In[ ]:




