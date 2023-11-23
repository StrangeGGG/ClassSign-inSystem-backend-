import mysql.connector
import pandas as pd
from tkinter import Tk, filedialog
import os
from sqlalchemy import create_engine

def main():
    # Open a file dialog for the user to select an Excel file
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename(title='Select input Excel file', filetypes=[('Excel Files', '*.xlsx')])
    root.destroy()

    # Read the Excel file
    df = pd.read_excel(file_path)

    # Connect to the MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="elec498g7",
        database="database_v1"
    )
    mycursor = mydb.cursor()
    # mycursor.execute("CREATE DATABASE database_v2")

    # Get the table name from the Excel file name
    table_name = os.path.splitext(os.path.basename(file_path))[0]

    # Connect to the MySQL database
    engine = create_engine("mysql+mysqlconnector://root:elec498g7@localhost/database_v2")

    # Write the data to the database
    df.to_sql(table_name, con=engine, if_exists='replace', index=False) # do not add index

    print(f"Data from {file_path} has been written to the {table_name} table in the database.")


if __name__ == '__main__':
    main()

