from Connector import create_connection

mydb = create_connection()

mycursor = mydb.cursor()

student_id = input("ID: ")

mycursor.execute("UPDATE names_and_sign_ins SET `Sign-in-Count` = `Sign-in-Count` + 1 WHERE ID = %s", (student_id,))

mydb.commit()

mydb.close()
