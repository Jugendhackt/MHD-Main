import sqlite3
from insert_functions import *

conn = sqlite3.connect('mhd.db')
print("Opened database successfully")

delete_from_table("PROTOCOLL", "USERS")

insert_user(1, "Paul", "123")
insert_user(2, "Niklas", "456")

insert_entry(2, '10.9.2021', '01.06.2021', 30)
conn.close()