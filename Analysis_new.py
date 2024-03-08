import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('ExampleData.xlsx')



def sum_sign_in_count(lst):
    return sum(lst)


df['Attendance Rate'] = df['Total-Count'] / df['Class_num_finished']


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
