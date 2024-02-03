import pandas as pd
import numpy as np
from flask_login import UserMixin
import ast


class User(UserMixin):
    def __init__(self, student_id, first_name, last_name):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.sign_count = np.array([], dtype=int)  # 初始设为空数组
        self.input_count = 0

    def update_sign_in(self):
        if not np.any(self.sign_count):  # 只有在数组为空的情况下才生成数组
            self.sign_count = np.array([0], dtype=int)
        else:
            self.sign_count = np.append(self.sign_count, 0)  # 随着输入次数的增加而增加
        self.input_count += 1


# 全局变量用于记录总的输入次数
total_input_count = 0


def read_users_from_excel(file_path):
    df = pd.read_excel(file_path)

    users_data = df.to_dict(orient='records')

    # Correcting the array format before evaluation
    users = {}
    for user in users_data:
        user_id = str(user['ID'])
        sign_count_value = user['Sign-in-Count']

        if pd.isna(sign_count_value):  # 如果是空值
            sign_count = np.array([], dtype=int)
        else:
            sign_count_str = str(sign_count_value).strip()  # 转换为字符串并移除可能存在的额外空格
            sign_count = np.array(ast.literal_eval(sign_count_str), dtype=int)

        users[user_id] = User(user_id, user['First Name'], user['Last Name'])
        users[user_id].sign_count = sign_count

    # Print user information
    for user_id, user in users.items():
        user.update_sign_in()  # Ensure an empty array is present for each user
        print(
            f"User ID: {user.id}, First Name: {user.first_name}, Last Name: {user.last_name}, Sign-in-Count: {user.sign_count}")

    return users


# 模拟用户的输入
def simulate_user_input(users):
    global total_input_count
    # 每次模拟用户输入时，更新用户的签到信息
    for user_id, user in users.items():
        user.update_sign_in()
        print(
            f"User ID: {user.id}, First Name: {user.first_name}, Last Name: {user.last_name}, Sign-in-Count: {user.sign_count}")

    # 更新全局的输入次数
    total_input_count += 1


# 不保存用户信息到 Excel
def save_users_to_excel(users, output_file_path):
    user_data = {
        'ID': [],
        'First Name': [],
        'Last Name': [],
        'Sign-in-Count': [],
    }

    for user_id, user in users.items():
        user_data['ID'].append(user.id)
        user_data['First Name'].append(user.first_name)
        user_data['Last Name'].append(user.last_name)
        user_data['Sign-in-Count'].append(user.sign_count)

    user_df = pd.DataFrame(user_data)
    user_df.to_excel(output_file_path, index=False)
    print(f"User data saved to {output_file_path}")


# Example usage
# file_path = "Extract.xlsx"
# output_file_path = "User_Data_Output.xlsx"
# users = read_users_from_excel(file_path)

file_path = "./User_Data_Output.xlsx"
output_file_path = "./User_Data_Output1.xlsx"
users = read_users_from_excel(file_path)

# 模拟用户每次开始计数的输入
input("Press Enter to simulate user input...")  # 一行告诉输入
simulate_user_input(users)

# 输出总的输入次数
print(f"Total Input Count: {total_input_count}")
