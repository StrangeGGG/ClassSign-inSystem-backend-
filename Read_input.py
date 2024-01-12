from Connector import create_connection

mydb = create_connection()
mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# print("Databases:")
# for x in mycursor:
#     print(x)

mycursor.execute("DESCRIBE names_and_sign_ins")
for column in mycursor:
    print(column)

mycursor.execute("SHOW TABLES")
print("\nTables:")
for x in mycursor:
    print(x)
# # add primary key
# mycursor.execute("ALTER TABLE names_and_sign_ins ADD PRIMARY KEY (ID)")
mycursor.execute("SELECT * FROM names_and_sign_ins")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
