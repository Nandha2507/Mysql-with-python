#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    mydb.close()
except Exception as e:
    print(str(e))


# In[5]:


import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost",user="root", passwd="mysql",use_pure=True)
    # check if the connection is established

    query = "SHOW DATABASES"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print(cursor.fetchall())

except Exception as e:
    mydb.close()
    print(str(e))


# In[4]:


import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())

    query = "Create database Student;"
    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Database Created!!")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))


# In[6]:


import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database = 'Student',user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())

    query = "CREATE TABLE StudentDetails (Studentid INT(10) AUTO_INCREMENT PRIMARY KEY,FirstName VARCHAR(60),"             "LastName VARCHAR(60), RegistrationDate DATE,Class Varchar(20), Section Varchar(10))"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Table Created!!")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))


# In[7]:


import mysql.connector as connection

try:
    mydb = connection.connect(host="localhost", database = 'Student',user="root", passwd="mysql",use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    query = "INSERT INTO StudentDetails VALUES ('1132','Sachin','Kumar','1997-11-11','Eleventh','A')"

    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Values inserted into the table!!")
    mydb.commit()
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))


# In[8]:


import mysql.connector as connection


try:
    mydb = connection.connect(host="localhost", database = 'GlassData',user="root", passwd="mysql",use_pure=True)
    #check if the connection is established
    print(mydb.is_connected())
    query = "Select * from GlassData;"
    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)
    mydb.close() #close the connection


except Exception as e:
    #mydb.close()
    print(str(e))


# In[9]:


import mysql.connector as connection
import pandas as pandas

try:

    mydb = connection.connect(host="localhost", database='Student', user="root", passwd="mysql", use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    query = "UPDATE studentdetails SET FirstName = 'Kumar', LastName = 'Gaurav' WHERE Studentid = 1122"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    mydb.commit()

    #let's check if the value is updated in the table.
    query = "Select * from studentdetails where Studentid=1122;"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)

    mydb.close()  # close the connection

except Exception as e:
    #mydb.close()
    print(str(e))


# In[10]:


import mysql.connector as connection
import pandas as pandas

try:

    mydb = connection.connect(host="localhost", database='GlassData', user="root", passwd="mysql", use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    query = "Select * from GlassData;"
    result_dataFrame = pandas.read_sql(query,mydb)
    print(result_dataFrame)

    mydb.close()  # close the connection

except Exception as e:
    #mydb.close()
    print(str(e))


# In[15]:


import mysql.connector as connection


try:
    mydb = connection.connect(host="localhost", database = 'GlassData',user="root", passwd="mysql",use_pure=True)
    #check if the connection is established
    print(mydb.is_connected())
    query = "Select * from GlassData;"
    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)
    mydb.close() #close the connection


except Exception as e:
    #mydb.close()
    print(str(e))


# In[13]:


import mysql.connector as connection

try:

    mydb = connection.connect(host="localhost", database='Student', user="root", passwd="mysql", use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())
    query = "DELETE FROM studentdetails WHERE Studentid = 1122"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    mydb.commit()

    #let's check if the value is updated in the table.
    query = "Select * from studentdetails where Studentid=1122;"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)

    mydb.close()  # close the connection

except Exception as e:
    #mydb.close()
    print(str(e))


# In[14]:


import mysql.connector as connection
import pandas as pandas
import csv

try:
    mydb = connection.connect(host="localhost", user="root", passwd="mysql",use_pure=True)
    #check if the connection is established
    print(mydb.is_connected())
    #create a new database
    query = "Create database GlassData;"
    cursor = mydb.cursor() #create a cursor to execute queries
    cursor.execute(query)
    print("Database Created!!")
    mydb.close() #close the connection

    #Establish a new connection to the database created above
    mydb = connection.connect(host="localhost", database = 'GlassData',user="root", passwd="mysql", use_pure=True)

    #create a new table to store glass data
    query = "CREATE TABLE IF NOT EXISTS GlassData (Index_Number INT(10),RI float(10,5), Na float(10,5), Mg float(10,5),Al float(10,5),"             " Si float(10,5), K float(10,5), Ca float(10,5), Ba float(10,5), Fe float(10,5), Class INT(5))"
    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    print("Table Created!!")

    #read from the file
    with open('glass.data', "r") as f:
        next(f)
        glass_data = csv.reader(f, delimiter="\n")
        for line in enumerate(glass_data):
            for list_ in (line[1]):
                cursor.execute('INSERT INTO GlassData values ({values})'.format(values=(list_)))
    print("Values inserted!!")
    mydb.commit()
    cursor.close()
    mydb.close()

except Exception as e:
    #mydb.close()
    print(str(e))


# In[ ]:




