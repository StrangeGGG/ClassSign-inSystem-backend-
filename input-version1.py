# import pandas as pd
# import numpy as np
# from flask_login import UserMixin
# import ast
#
#
# class User(UserMixin):
#     def __init__(self, student_id, first_name, last_name):
#         self.id = student_id
#         self.first_name = first_name
#         self.last_name = last_name
#         self.sign_count = np.array([], dtype=int)
#         self.total_count = 0
#
#     def update_sign_in(self):
#         if not np.any(self.sign_count):
#             self.sign_count = np.array([0], dtype=int)
#         else:
#             self.sign_count = np.append(self.sign_count, 0)
#         self.total_count += 1
#
#
# def read_users_from_excel(file_path):
#     df = pd.read_excel(file_path)
#     users_data = df.to_dict(orient='records')
#
#     users = {}
#     for user in users_data:
#         user_id = str(user['ID'])
#         sign_count_value = user['Sign-in-Count']
#
#         if pd.isna(sign_count_value):  # 如果是空值
#             sign_count = np.array([], dtype=int)
#         else:
#             sign_count_str = str(sign_count_value).strip()  # 转换为字符串并移除可能存在的额外空格
#             sign_count = np.array(ast.literal_eval(sign_count_str), dtype=int)
#
#         users[user_id] = User(user_id, user['First Name'], user['Last Name'])
#         users[user_id].sign_count = sign_count
#
#     for user_id, user in users.items():
#         user.update_sign_in()  # Ensure an empty array is present for each user
#         print(
#             f"User ID: {user.id}, First Name: {user.first_name}, Last Name: {user.last_name}, Sign-in-Count: {user.sign_count}")
#
#     return users
#
#
# def simulate_user_input(users):
#     df_saved = pd.read_excel(file_path)
#     total_count_from_excel = df_saved['Total-Count'][0]
#
#     total_count_from_excel += 1
#
#     user_choice = input("Press Enter to simulate user input, or press 1 to skip: ")
#
#     if user_choice != '1':
#         for user_id, user in users.items():
#             user.update_sign_in()
#             user.total_count = total_count_from_excel
#             print(
#                 f"User ID: {user.id}, First Name: {user.first_name}, Last Name: {user.last_name}, Sign-in-Count: {user.sign_count}, Total-Count: {user.total_count}")
#     else:
#         print("Skipping user input simulation.")
#     save_users_to_excel(users, output_file_path, total_count_from_excel)
#
# def simulate_user_input(users):
#     global total_input_count
#
#     df_saved = pd.read_excel(file_path)
#     total_count_from_excel = df_saved['Total-Count'][0]
#
#     total_input_count = total_count_from_excel + 1
#
#     input("Press Enter to simulate user input, or press 1 to skip: ")
#
#     for user_id, user in users.items():
#         user.update_sign_in()
#         user.total_count = total_count_from_excel  # 使用读取的 Total-Count 值
#         print(
#             f"User ID: {user.id}, First Name: {user.first_name}, Last Name: {user.last_name}, Sign-in-Count: {user.sign_count}, Total-Count: {user.total_count}")
#
#
# def save_users_to_excel(users, output_file_path, total_count):
#     user_data = {
#         'ID': [],
#         'First Name': [],
#         'Last Name': [],
#         'Sign-in-Count': [],
#         'Total-Count': []
#     }
#
#     for user_id, user in users.items():
#         user_data['ID'].append(user.id)
#         user_data['First Name'].append(user.first_name)
#         user_data['Last Name'].append(user.last_name)
#
#         # 更新 Sign-in-Count 列，确保数组长度与 Total-Count 相匹配
#         sign_in_count = user.sign_count.tolist() + [0] * (int(total_count) - len(user.sign_count))
#         user_data['Sign-in-Count'].append(sign_in_count)
#
#         # 更新 Total-Count 列，只更新第一行
#         user_data['Total-Count'].append(total_count if not user_data['Total-Count'] else np.nan)
#
#     user_df = pd.DataFrame(user_data)
#
#     user_df.to_excel(output_file_path, index=False)
#     print(f"User data saved to {output_file_path}")
#
#
#
# # Example usage
# file_path = "./User_Data_Output2.xlsx"
# output_file_path = "./User_Data_Output3.xlsx"
# users = read_users_from_excel(file_path)
#
#
#
# simulate_user_input(users)
#
#
# save_users_to_excel(users, output_file_path, total_input_count)



import pandas as pd
import numpy as np
from flask_login import UserMixin
import ast


class User(UserMixin):
    def __init__(self, student_id, first_name, last_name):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.sign_count = np.array([], dtype=int)
        self.total_count = 0

    def update_sign_in(self):
        if not np.any(self.sign_count):
            self.sign_count = np.array([0], dtype=int)
        else:
            self.sign_count = np.append(self.sign_count, 0)
        self.total_count += 1


def read_users_from_excel(file_path):
    df = pd.read_excel(file_path)
    users_data = df.to_dict(orient='records')

    users = {}
    for user in users_data:
        user_id = str(user['ID'])
        sign_count_value = user['Sign-in-Count']

        if pd.isna(sign_count_value):
            sign_count = np.array([], dtype=int)
        else:
            sign_count_str = str(sign_count_value).strip()  # 转换为字符串并移除可能存在的额外空格
            sign_count = np.array(ast.literal_eval(sign_count_str), dtype=int)

        users[user_id] = User(user_id, user['First Name'], user['Last Name'])
        users[user_id].sign_count = sign_count

    for user_id, user in users.items():
        user.update_sign_in()
        print(
            f"User ID: {user.id}, First Name: {user.first_name}, Last Name: {user.last_name}, Sign-in-Count: {user.sign_count}")

    return users


def simulate_user_input(users):
    global total_input_count

    df_saved = pd.read_excel(file_path)
    total_count_from_excel = df_saved['Total-Count'][0]

    user_choice = input("Press Enter to simulate user input, or press 's' to skip: ")

    if user_choice.lower() != 's':
        total_input_count = total_count_from_excel + 1

        for user_id, user in users.items():
            user.update_sign_in()
            user.total_count = total_count_from_excel  # 使用读取的 Total-Count 值
            print(
                f"User ID: {user.id}, First Name: {user.first_name}, Last Name: {user.last_name}, Sign-in-Count: {user.sign_count}, Total-Count: {user.total_count}")

        save_users_to_excel(users, output_file_path, total_input_count)
    else:
        print("Skipping user input simulation.")


def save_users_to_excel(users, output_file_path, total_count):
    user_data = {
        'ID': [],
        'First Name': [],
        'Last Name': [],
        'Sign-in-Count': [],
        'Total-Count': []
    }

    for user_id, user in users.items():
        user_data['ID'].append(user.id)
        user_data['First Name'].append(user.first_name)
        user_data['Last Name'].append(user.last_name)

        sign_in_count = user.sign_count.tolist() + [0] * (int(total_count) - len(user.sign_count))
        user_data['Sign-in-Count'].append(sign_in_count)

        user_data['Total-Count'].append(total_count if not user_data['Total-Count'] else np.nan)

    user_df = pd.DataFrame(user_data)

    user_df.to_excel(output_file_path, index=False)
    print(f"User data saved to {output_file_path}")


# Example usage
file_path = "Extract.xlsx"
output_file_path = "./User_Data_Output.xlsx"
users = read_users_from_excel(file_path)

simulate_user_input(users)


