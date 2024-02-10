import pandas as pd
import matplotlib.pyplot as plt

# 读取 Excel 文件
df = pd.read_excel('DataAnalysis.xlsx')

# 将 'Sign-in-Count' 列中的字符串转换为数字
df['Sign-in-Count'] = df['Sign-in-Count'].apply(lambda x: eval(x))

# 计算 'Sign-in-Count' 列中列表值的和
def sum_sign_in_count(lst):
    return sum(lst)

# 将 'Sign-in-Count' 列中的列表值求和并创建新列
df['Sign-in-Count_Sum'] = df['Sign-in-Count'].apply(sum_sign_in_count)

# 计算签到率
df['Attendance Rate'] = df['Sign-in-Count_Sum'] / df['Total Count']

# 将签到率写入原始 Excel 文件中
df.to_excel('DataAnalysis_with_Attendance_Rate.xlsx', index=False)

# 绘制图表
plt.figure(figsize=(10, 6))
plt.bar(df['First Name'], df['Attendance Rate'], color='skyblue')
plt.xlabel('First Name')
plt.ylabel('Attendance Rate')
plt.title('Attendance Rate of Each Person')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Attendance_Rate_Plot.png')  # 保存图像

# 显示图表
plt.show()
