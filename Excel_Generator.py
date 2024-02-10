import pandas as pd
import numpy as np

names = [
    "James Smith",
    "Olivia Johnson",
    "Emma Williams",
    "Ava Brown",
    "Sophia Jones",
    "Isabella Miller",
    "Mia Davis",
    "Charlotte Garcia",
    "Amelia Rodriguez",
    "Harper Martinez",
    "Evelyn Hernandez",
    "Abigail Moore",
    "Emily Taylor",
    "Elizabeth Anderson",
    "Sofia Thomas",
    "Avery Jackson",
    "Ella White",
    "Scarlett Harris",
    "Grace Martin",
    "Chloe Thompson",
    "Madison Garcia",
    "Eleanor Martinez",
    "Penelope Robinson",
    "Lily Clark",
    "Nora Rodriguez",
    "Riley Lewis",
    "Zoey Walker",
    "Victoria Hall",
    "Hazel Allen",
    "Natalie Young"
]

ids = list(range(1, 31))
sign_in_counts = [list(np.random.randint(2, size=30)) for _ in range(30)]

first_names = [name.split()[0] for name in names]
last_names = [name.split()[1] for name in names]

df = pd.DataFrame({
    'ID': ids,
    'First Name': first_names,
    'Last Name': last_names,
    'Sign-in-Count': sign_in_counts
})

# 转换数组为字符串表示，只放入方括号中
df['Sign-in-Count'] = df['Sign-in-Count'].apply(lambda x: '[' + ','.join(map(str, x)) + ']')

df.to_excel('DataAnalysis.xlsx', index=False)
