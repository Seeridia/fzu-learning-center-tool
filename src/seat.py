# 座位情况

import os
from src.core.query import query_seat_status
from src.core.time_validation import time_input

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    with open("token.txt", "r", encoding="utf-8") as f:
        token = f.read().strip()

    print("座位预约情况")
    print("——————————————————————————————————————————————")

    date, begin, end = time_input(False)

    query_seat_status(date, begin, end, token)

if __name__ == '__main__':
    main()