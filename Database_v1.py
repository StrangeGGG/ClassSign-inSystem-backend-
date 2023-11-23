# https://www.w3schools.com/python/python_mysql_insert.asp
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="elec498g7",
    database="database_v1"
)

print(mydb)

# creating a database
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE database_v1")

# check if database exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

# creating a table, table's name is students,
mycursor.execute("CREATE TABLE students (name VARCHAR(255))")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
# table already exists, add primary key id to the table, or can do follow then first creating the tabel
# mycursor.execute("CREATE TABLE students (id is the primary key, name VARCHAR(255))")
mycursor.execute("ALTER TABLE students ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") # add behind
# insert value
sql = "INSERT INTO students (name) VALUES (%s)"
# when using a single value to create a tuple, need a comma at the end; if more than one value, no comma at end
val = ('G',)
mycursor.execute(sql, val)

mydb.commit()  # like 'make' in Linux, to make the changes

print(mycursor.rowcount, "record inserted.")

# insert multiple rows
val = [
    ('Mike',),
    ('Peter',)
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
# get id
val = ('Michelle',)
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)  # last row's id

# select from a table
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# select columns
mycursor.execute("SELECT name FROM students")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# return the first row
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchone()
print(myresult)

# filter to select
sql = "SELECT * FROM students WHERE name = 'G'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# select starts, includes, or ends with a given letter, using %
sql = "SELECT * FROM students WHERE name LIKE '%e%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# prevent injection(web hacking)
sql = "SELECT * FROM students WHERE name = %s"
name = ("Mike",)
mycursor.execute(sql, name)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# sort result
sql = "SELECT * FROM students ORDER BY name"
# sql = "SELECT * FROM students ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# delete record
sql = "DELETE FROM students WHERE name = 'G'"
# prevent injection
# sql = "DELETE FROM students WHERE name = %s"
# name = ("G",)
# mycursor.execute(sql, name)
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# delete a table
sql = "DROP TABLE students"
# drop only if exists, avoid error if already delete or not exist
# sql = "DROP TABLE IF EXISTS students"
mycursor.execute(sql)

# update table
sql = "UPDATE students SET name = 'Milk' WHERE name = 'Mike'"
# prevent injection
# sql = "UPDATE students SET name = %s WHERE name = %s"
# val = ("Milk", "Mike")
# mycursor.execute(sql, val)
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

# limit the result
mycursor.execute("SELECT * FROM students LIMIT 3")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# # start from another position
# mycursor.execute("SELECT * FROM students LIMIT 1 OFFSET 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# usersGet
# { id: 1, name: 'John', fav: 154},
# { id: 2, name: 'Peter', fav: 154},
# { id: 3, name: 'Amy', fav: 155},
# { id: 4, name: 'Hannah', fav:},
# { id: 5, name: 'Michael', fav:}
# products
# { id: 154, name: 'Chocolate Heaven' },
# { id: 155, name: 'Tasty Lemons' },
# { id: 156, name: 'Vanilla Dreams' }

# # inner join
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"
# # left join
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"
# # right join
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   RIGHT JOIN products ON users.fav = products.id"