# 个人预约记录

import os
from src.core.history import view_personal_appointments

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    with open("token.txt", "r", encoding="utf-8") as f:
        token = f.read().strip()

    print("个人预约历史")
    print("—————————————————————————————————————————————————————————————")

    page = 1
    pageSize = 10

    while True:
        payload = {
            "currentPage": page,
            "pageSize": pageSize
        }

        response = view_personal_appointments(token, payload)

        if response.status_code != 200:
                print("请求失败，状态码：", response.status_code)
                break

        res_json = response.json()
        if res_json.get("code") != "0":
            print("接口返回错误：", res_json.get("msg"))
            break

        dataList = res_json.get("dataList", [])
        if not dataList:
            print("无预约记录。")
            break

        print(f"第 {page} 页预约记录:")
        print(" ID      座位号   预约时间                状态")
        print("——————————————————————————————————————————————")
        for record in dataList:
            appointment_time = f"{record.get('date', '')} {record.get('beginTime', '')}-{record.get('endTime', '')}"
            id = record.get('id', '')
            spaceName = record.get('spaceName', '')
            sign = record.get('sign', False)
            auditStatus = record.get('auditStatus', )
            floor = record.get('floor', 4)

            # 状态：
            # auditStatus: 2-待签到/已签到，3-已取消，4-已完成
            # sign: True-已签到，False-未签到

            if auditStatus == 3:
                status = "已取消"
            elif auditStatus == 4:
                status = "已完成"
            elif auditStatus == 2:
                status = "已签到" if sign else "待签到"
            else:
                status = "未知"

            print(f" {id}  {floor}F{spaceName}    {appointment_time}  {status}")

        if len(dataList) < pageSize:
            print("已是最后一页。")
            break

        choice = input("按N键继续下一页，其他键退出：")
        if choice.lower() != 'n':
            break
        page += 1

if __name__ == '__main__':
    main()