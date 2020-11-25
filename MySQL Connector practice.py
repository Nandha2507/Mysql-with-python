#!/usr/bin/env python
# coding: utf-8

# In[6]:


import mysql.connector as connection
try:
    mydb=connection.connect(host='localhost',user="root",passwd="Nandha11_nk")
    print(mydb.is_connected())
    mydb.close()
except Exception as e:
    print(str(e))
    


# In[13]:


try:
    import mysql.connector as connection
    
    mydb=connection.connect(host="localhost",user="root",passwd="Nandha11_nk")
    print(mydb.is_connected())
    
    query="show databases"
    
    cursor=mydb.cursor()
    cursor.execute(query)
    print(cursor.fetchall())
    
except Exception as e:
    mydb.close()
    print(str(e))


# In[16]:


try:
    import mysql.connector as connection
    
    db=connection.connect(host="localhost",user="root",passwd="Nandha11_nk")
    print(db.is_connected())
    
    query="create database student"
    
    cursor=db.cursor()
    cursor.execute(query)
    print("Database created successfully!!!")
    
except Exception as e:
    db.close()
    print(str(e))


# In[25]:


try:
    import mysql.connector as connection
    
    db=connection.connect(host="localhost",user="root",passwd="Nandha11_nk",database="student",use_pure=True)
    print(db.is_connected())
    
    query="CREATE TABLE StudentDetails (Studentid INT(10) AUTO_INCREMENT PRIMARY KEY,FirstName VARCHAR(60),"             "LastName VARCHAR(60), RegistrationDate DATE,Class Varchar(20), Section Varchar(10))"
        
    cursor=db.cursor()
    cursor.execute(query)
    print("Table created sucessfully!!!")

except Exception as e:
    print(str(e))    


# In[35]:


try:
    import mysql.connector as connection
    
    db=connection.connect(host="localhost",user="root",passwd="Nandha11_nk",database="student",use_pure=True)
    print(db.is_connected())
    
    query="INSERT INTO StudentDetails VALUES ('1100','Sachin','Kumar','1997-11-11','Eleventh','A')"
    
    cursor=db.cursor()
    cursor.execute(query)
    print("Value inserted..")
    db.commit()
    db.close()
    
except Exception as e:
    db.close()
    print(str(e))
        


# In[38]:


try:
    import mysql.connector as connection
    db=connection.connect(host="localhost",user="root",passwd="Nandha11_nk",database="student")
    print(db.is_connected())
    
    query="Select * from StudentDetails;"
    
    cursor=db.cursor()
    cursor.execute(query)
    for result in cursor.fetchall():
        print(result)
    db.close()
    
except Exception as e:
    db.close()
    print(str(e))


# In[9]:


import mysql.connector as connection


# In[15]:


db=connection.connect(host="localhost",user="root",passwd="Nandha11_nk",database="nk")


# In[16]:


db.is_connected()


# In[17]:


query="select * from iris"


# In[18]:


cursor=db.cursor()
cursor.execute(query)


# In[19]:


for a in cursor.fetchall():
    print(a)


# In[ ]:




