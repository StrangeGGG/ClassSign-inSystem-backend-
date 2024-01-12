import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="elec498g7",
    database="database_v2"
)

mycursor = mydb.cursor()

student_id = input("ID: ")

mycursor.execute("SELECT * FROM names_and_sign_ins WHERE ID = %s", (student_id,))
result = mycursor.fetchone()

if result is not None:
    mycursor.execute("UPDATE names_and_sign_ins SET `Sign-in-Count` = `Sign-in-Count` + 1 WHERE ID = %s", (student_id,))
    print("Successfully sign in")
    mydb.commit()
else:
    print("Failed sign in, no student information")