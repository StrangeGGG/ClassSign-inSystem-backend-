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


# from flask import Flask, render_template, request, redirect, url_for
# from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
# from datetime import datetime
# import pandas as pd
#
# app = Flask(__name__)
# app.secret_key = "111111"
# login_manager = LoginManager()
# login_manager.init_app(app)
#
#
# class User(UserMixin):
#     def __init__(self, student_id, first_name, last_name, sign_count):
#         self.id = student_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.sign_count = sign_count
#
#
# def read_users_from_excel(file_path):
#     df = pd.read_excel(file_path)
#
#     users_data = df.to_dict(orient='records')
#     users = {str(user['ID']): User(str(user['ID']), user['First Name'], user['Last Name'], user['Sign-in-Count']) for
#              user in users_data}
#
#     return users
#
#
# def save_user_data_to_excel(users, new_user):
#     user_data = {
#         'ID': [new_user.id],
#         'First Name': [new_user.first_name],
#         'Last Name': [new_user.last_name],
#         'Sign-in-Count': [new_user.sign_count]
#     }
#
#     try:
#         df = pd.read_excel('./names_and_sign_ins.xlsx')
#     except FileNotFoundError:
#         df = pd.DataFrame(user_data)
#
#     df = pd.concat([df, pd.DataFrame(user_data)], ignore_index=True)
#     df.to_excel('./Extract.xlsx', index=False)
#
#
# @login_manager.user_loader
# def user_loader(id):
#     return users.get(id)
#
#
# @app.route('/')
# def home():
#     return render_template('./index.html')
#
#
# @app.post('/login')
# def login():
#     name = request.form.get('studentFirstName')
#     login_id = request.form.get('studentId')
#
#     user = users.get(login_id)
#
#     if user is None or user.first_name != name:
#         return redirect(url_for('home'))
#     login_user(user, remember=True)
#     return redirect(url_for('user_info', user_name=name, user_id=login_id))
#
#
# @app.route('/info/<user_name>/<int:user_id>')
# @login_required
# def user_info(user_name, user_id):
#     time = datetime.now().strftime("%H:%M:%S")
#     save_user_data_to_excel(user_id, user_name)
#     return render_template('./signin.html', name=user_name, id=user_id, time=time)
#
#
# @app.route("/logout")
# def logout():
#     logout_user()
#     return "Logged out"
#
#
# if __name__ == '__main__':
#     # excel_file_path = './names_and_sign_ins.xlsx'
#     # users = read_users_from_excel(excel_file_path)
#
#     app.run(host='0.0.0.0', port=8000)








