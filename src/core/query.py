import os
import requests
import json
import pandas as pd

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

    df_4F = pd.DataFrame(json_data_4F.get('dataList', []))
    df_5F = pd.DataFrame(json_data_5F.get('dataList', []))
    df = pd.concat([df_4F, df_5F], ignore_index=True)
    df = df[['id', 'spaceCode', 'spaceName', 'floor', 'spaceStatus']]

    df = df[~df['spaceName'].str.contains('-')]
    df['spaceName'] = df['spaceName'].str.zfill(3)
    df = df.sort_values('spaceName')
    df.to_csv("space_status.csv", index=False, encoding="utf-8")
    print("已生成 space_status.csv")

    os.remove(file_4F)
    os.remove(file_5F)
    
    os.system('cls' if os.name == 'nt' else 'clear')

    status_counts = df['spaceStatus'].value_counts()
    total = len(df)
    free = status_counts.get(0, 0)
    temp_df = df[df['spaceName'].astype(int).between(205, 476)]
    free_sinfgle = len(temp_df[temp_df['spaceStatus'] == 0])

    print("统计项            数量        占比")
    print("——————————————————————————————————")
    print(f"总座位数         {total}       100.0%")
    print(f"空闲座位数       {free}        {free / total:.1%}")
    print(f"空闲单人座位数    {free_sinfgle}         {free_sinfgle / total:.1%}")

    while True:
        print("\n")
        print("   [1]   查看空闲座位")
        print("   [2]   查看空闲单人座位")
        print("   [3]   返回")
        choice = input("\n请输入你的选择: ")
        if choice == "1":
            print("\n空闲座位列表")
            print("——————————————————————————————————")
            free_seats = df[df['spaceStatus'] == 0]['spaceName'].tolist()
            for i in range(0, len(free_seats), 15):
                print(' '.join(free_seats[i:i+15]))
        elif choice == "2":
            print("\n空闲单人座位列表")
            print("——————————————————————————————————")
            free_single_seats = temp_df[temp_df['spaceStatus'] == 0]['spaceName'].tolist()
            for i in range(0, len(free_single_seats), 15):
                print(' '.join(free_single_seats[i:i+15]))
        elif choice == "3":
            return
        else:
            print("输入错误，请重新输入")

