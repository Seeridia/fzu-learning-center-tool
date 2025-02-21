import os
import datetime
from core.query import query_seat_status
from core.time_validation import time_input

os.system('cls' if os.name == 'nt' else 'clear')

with open("token.txt", "r", encoding="utf-8") as f:
    token = f.read().strip()

print("座位预约情况")
print("——————————————————————————————————————————————")

date, begin, end = time_input(False)

# 调用查询模块函数执行座位查询
if query_seat_status(date, begin, end, token):
    print("查询成功，座位信息已返回。")
else:
    print("查询失败，请检查输入的时间或座位状态。")
