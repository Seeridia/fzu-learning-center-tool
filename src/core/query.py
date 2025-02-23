import os
import requests
import json

url = "https://aiot.fzu.edu.cn/api/ibs/spaceAppoint/app/queryStationStatusByTime"

def query_floor_data(floor_like, beginTime, endTime, token):
    file_name = f"{floor_like}F.json"
    payload = {
        "beginTime": beginTime,
        "endTime": endTime,
        "floorLike": floor_like,
        "parentId": None,
        "region": 1
    }
    headers = {"token": token}
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        try:
            data = response.json()
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"已获取 {file_name} 数据")
        except json.JSONDecodeError:
            print("无法解析 JSON 响应", response.text)
    else:
        print(f"请求失败，状态码：{response.status_code}", response.text)
    return file_name

def query_seat_status(parsed_date, begin_hour, end_hour, token):
    beginTime_input = f"{parsed_date} {begin_hour}"
    endTime_input = f"{parsed_date} {end_hour}"
    print(f"正在获取 {parsed_date} {begin_hour}-{end_hour} 的 座位状态数据...")

    file_4F = query_floor_data("4", beginTime_input, endTime_input, token)
    file_5F = query_floor_data("5", beginTime_input, endTime_input, token)

    with open(file_4F, "r", encoding="utf-8") as file:
        json_data_4F = json.load(file)
    with open(file_5F, "r", encoding="utf-8") as file:
        json_data_5F = json.load(file)

    combined_data = []
    for data in [json_data_4F, json_data_5F]:
        combined_data.extend(data.get('dataList', []))

    filtered_data = []
    fields = ['id', 'spaceCode', 'spaceName', 'floor', 'spaceStatus']
    for item in combined_data:
        if '-' not in item.get('spaceName', ''):
            new_item = {k: item.get(k) for k in fields}
            new_item['spaceName'] = new_item['spaceName'].zfill(3)
            filtered_data.append(new_item)

    filtered_data = sorted(filtered_data, key=lambda x: int(x['spaceName']))

    os.remove(file_4F)
    os.remove(file_5F)
    
    os.system('cls' if os.name == 'nt' else 'clear')

    total = len(filtered_data)
    free = sum(1 for item in filtered_data if item['spaceStatus'] == 0)
    temp_data = [item for item in filtered_data 
                if 205 <= int(item['spaceName']) <= 476]
    free_single = sum(1 for item in temp_data if item['spaceStatus'] == 0)

    print("统计项            数量        占比")
    print("——————————————————————————————————")
    print(f"总座位数         {total}       100.0%")
    print(f"空闲座位数       {free}        {free / total:.1%}")
    print(f"空闲单人座位数    {free_single}         {free_single / total:.1%}")
    print(f"\n统计时间段: {parsed_date} {begin_hour}-{end_hour}")

    if free == 0:
        print("\n所有座位已被预约了喵~")
        print("我知道你不信，但是结果就是这样的喵~")
        print("不过也有可能是因为你在这时候约过座位啦，所以就不让你再约一次了... ＞﹏＜")
        print("大馋猫！")
    elif free_single == 0:
        print("\n所有单人座位已被预约了喵~")
        print("只好和别人一起学习了...")
        print("如果是其他小猫，你可别忘记我了喵 (ಥ _ ಥ)")

    while True:
        print("\n")
        if free > 0:
            print("   [1]   查看空闲座位")
        else:
            print("   [1]   查看空闲座位(你点了不会多出来的喵~)")

        if free_single > 0:
            print("   [2]   查看空闲单人座位")
        else:
            print("   [2]   查看空闲单人座位(你点了不会多出来的喵~)")
        
        print("   [3]   返回")
        choice = input("\n请输入你的选择: ")

        if choice == "1":
            if free == 0:
                print("\n坏蛋！都让你别点了！真的没有了！一点都没有！")
                continue
            print("\n空闲座位列表")
            print("——————————————————————————————————")
            free_seats = [item['spaceName'] for item in filtered_data 
                        if item['spaceStatus'] == 0]
            for i in range(0, len(free_seats), 15):
                print(' '.join(free_seats[i:i+15]))
        elif choice == "2":
            if free_single == 0:
                print("\n坏蛋！都让你别点了！真的没有了！一点都没有！")
                continue
            print("\n空闲单人座位列表")
            print("——————————————————————————————————")
            free_single_seats = [item['spaceName'] for item in temp_data 
                                if item['spaceStatus'] == 0]
            for i in range(0, len(free_single_seats), 15):
                print(' '.join(free_single_seats[i:i+15]))
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        else:
            print("输入错误，请重新输入")

