import pandas as pd
import random

# 这是您的名字列表
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

# 创建ID和签到次数列表
ids = list(range(1, 31))
sign_in_counts = [random.randint(1, 30) for _ in range(30)]

# 创建一个数据框架
df = pd.DataFrame({
    'ID': ids,
    'Name': names,
    'Sign-in Count': sign_in_counts
})

# 将数据框架写入Excel文件
df.to_excel('names_and_sign_ins.xlsx', index=False)