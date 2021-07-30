# Higher/Lower Game
import sys
import os
import random

sys.path.append(
    "C:/Users/Milos Subak/OneDrive/VS Code projects/_Python_sandbox/Art/")

from higher_lower import logo
from higher_lower_data import data

os.system("cls")
print(logo)

account_a = random.choice(data)
account_b = random.choice(data)

if account_a == account_b:
    account_b = random.choice(data)

print(account_a, account_b)
