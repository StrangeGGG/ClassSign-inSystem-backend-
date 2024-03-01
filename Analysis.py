import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('DataAnalysis.xlsx')


df['Sign-in-Count'] = df['Sign-in-Count'].apply(lambda x: eval(x))


def sum_sign_in_count(lst):
    return sum(lst)


df['Sign-in-Count_Sum'] = df['Sign-in-Count'].apply(sum_sign_in_count)


df['Attendance Rate'] = df['Sign-in-Count_Sum'] / df['Total Count']


df.to_excel('DataAnalysis_with_Attendance_Rate.xlsx', index=False)


plt.figure(figsize=(10, 6))
plt.bar(df['First Name'], df['Attendance Rate'], color='skyblue')
plt.xlabel('First Name')
plt.ylabel('Attendance Rate')
plt.title('Attendance Rate of Each Person')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Attendance_Rate_Plot.png')


plt.show()
