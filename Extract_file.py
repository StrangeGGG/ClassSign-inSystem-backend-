from Connector import create_connection
import pandas as pd

mydb = create_connection()
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM names_and_sign_ins")
rows = mycursor.fetchall()
# change to pandas DataFrame
df = pd.DataFrame(rows, columns=
                  [i[0] for i in
                   mycursor.description])

df.to_excel("Extract.xlsx", index=False)

print("Extraction is finished")