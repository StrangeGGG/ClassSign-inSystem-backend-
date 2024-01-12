from Connector import create_connection

mydb = create_connection()

mycursor = mydb.cursor()

student_id = input("ID: ")
first_name = input("First Name: ")

mycursor.execute("SELECT * FROM names_and_sign_ins WHERE ID = %s AND `First Name` = %s", (student_id, first_name))
result = mycursor.fetchone()

if result is not None:
    mycursor.execute("UPDATE names_and_sign_ins SET `Sign-in-Count` = `Sign-in-Count` + 1 WHERE ID = %s", (student_id,))
    print("Successfully signed in")
    mydb.commit()
else:
    print("Failed sign in, no student information or incorrect first name")