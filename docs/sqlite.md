A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.

2 main types of databases
    -> SQL: MySQL, MariaDB, SQLite
    -> NoSQL: CouchDB, MongoDB

Python has libraries which can read/write from/in a DB. The following examples will be with sqlite

**How to create a table**
```
import sqlite3

#connect to the DB
connection = sqlite3.connect('my_database.db')
cursor = conn.cursor()

#create table users
cursor.execute("CREATE TABLE users (name text, email text)")

#commit the changes to db
connection.commit()
#close the connection
connection.close()
```

**How to read**
```
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
connection.close()

dict = [{'name': x[0], 'email': x[1]} for x in users]
```

**How to add**
```
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

command = "INSERT INTO users (name, email) VALUES ('%s', '%s')" \  
          % (user_info['name'], user_info['email'])
cursor.execute(command)
connection.close()
```

**How to delete**
```
import sqlite3

# with closes automatically the connection, it can also be used when opening a file
with sqlite3.connect('my_database.db') as connection:  
    cursor = connection.cursor()  
    command = f"DELETE FROM users WHERE name = '{user_name}'"  
    cursor.execute(command)  
    connection.commit()
```

**How to edit**
```
import sqlite3

with sqlite3.connect('my_database.db') as connection:  
    cursor = connection.cursor()
    command = f"UPDATE users SET email='{user_email}' WHERE name='{user_name}'"
    cursor.execute(command)
    connection.commit()
```


Additional links:

https://docs.python.org/3/library/sqlite3.html

https://realpython.com/python-sqlite-sqlalchemy/

https://vegibit.com/python-sqlite3-tutorial/

https://datagy.io/python-sqlite-tutorial/

