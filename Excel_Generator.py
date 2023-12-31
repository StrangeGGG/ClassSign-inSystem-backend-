import pandas as pd
import random

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
sign_in_counts = [random.randint(1, 30) for _ in range(30)]

df = pd.DataFrame({
    'ID': ids,
    'Name': names,
    'Sign-in Count': sign_in_counts
})

df.to_excel('names_and_sign_ins.xlsx', index=False)