import requests

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

    return response