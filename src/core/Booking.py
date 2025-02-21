import requests
import os
from core.IDConversion import get_space_name_by_id

url = "https://aiot.fzu.edu.cn/api/ibs/spaceAppoint/app/addSpaceAppoint"

def book_seat(date, begin, end, seat, token):
    payload = {
        "spaceId": int(seat),
        "beginTime": begin,
        "endTime": end,
        "date": date.isoformat()  # 将日期转换为字符串格式
    }

    headers = {
        "token": token
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.json().get('msg') == "成功":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("预约成功")
        print("————————————————————————")
        print(f"座位: {str(get_space_name_by_id(int(seat))).zfill(3)}")
        print(f"时间: {date} {begin}-{end}\n")
        # TODO：打印预约成功后的预约ID
    else:
        print(f"预约失败: {response.json().get('msg')}")