import pandas as pd
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

excel_file_path = './names_and_sign_ins.xlsx'
users = read_users_from_excel(excel_file_path)

for user_id, user in users.items():
    print(f"User ID: {user_id}, Name: {user.first_name} {user.last_name}, Sign Count: {user.sign_count}")