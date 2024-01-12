import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="elec498g7",
    database="database_v2"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM names_and_sign_ins")
rows = mycursor.fetchall()
# change to pandas DataFrame
df = pd.DataFrame(rows, columns=
                  [i[0] for i in
                   mycursor.description])

df.to_excel("Extract.xlsx", index=False)