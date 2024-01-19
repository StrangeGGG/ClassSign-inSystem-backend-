import pandas as pd
import numpy as np
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, student_id, first_name, last_name, sign_count):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.sign_count = sign_count

def read_users_from_excel(file_path):
    df = pd.read_excel(file_path)

    users_data = df.to_dict(orient='records')
    users = {str(user['ID']): User(str(user['ID']), user['First Name'], user['Last Name'], user['Sign-in-Count']) for user in users_data}

    return users

def convert_sign_count_to_array(df, column_name, array_length):
    if 'Sign-in-Count' in df.columns:
        sign_count_array = np.pad(df['Sign-in-Count'].values, (0, array_length - len(df['Sign-in-Count'])), 'constant')
    else:
        sign_count_array = np.zeros(array_length, dtype=int)

    # Drop the 'Sign-in-Count' column if it exists
    if 'Sign-in-Count' in df.columns:
        df = df.drop(columns=['Sign-in-Count'])

    df[column_name] = [sign_count_array] * len(df)

    return df

excel_file_path = './names_and_sign_ins.xlsx'
df = pd.read_excel(excel_file_path)

df = convert_sign_count_to_array(df, 'Sign_Count_Array', 40)

df.to_excel('./Extract.xlsx', index=False)
