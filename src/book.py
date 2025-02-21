import os
from core.Booking import book_seat
from core.time_validation import time_input
from core.IDConversion import get_id_by_space_name

os.system('cls' if os.name == 'nt' else 'clear')

with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read().strip()

print("座位预约")
print("——————————————————————————————————————————————")

date, begin, end = time_input(True)

while True:
    space_name = input("请输入座位号: ")
    id = get_id_by_space_name(space_name)
    
    if id:
        break
    else:
        print("座位编号无效，请重新输入。")

book_seat(date, begin, end, id, token)