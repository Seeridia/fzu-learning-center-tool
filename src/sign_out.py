import os
from src.core.operation import operate
from src.core.history import view_personal_appointments

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("签退")
    print("——————————————————————————————————————————————")

    with open("token.txt", "r", encoding="utf-8") as f:
        token = f.read().strip()

    payload = {
        "currentPage": 1,
        "pageSize": 10
    }

    history = view_personal_appointments(token, payload).json()

    dataList = history.get("dataList", [])

    has_signable = False
    for record in dataList:
        if record.get('auditStatus') == 2 and record.get('sign') == True :
            has_signable = True
            print(f"发现可签退的预约：{record.get('date')} {record.get('beginTime')}-{record.get('endTime')}")
            confirm = input("是否进行签退？(y/n): ")
            if confirm.lower() == 'y':
                print(f"正在签退...")
                response = operate(token, "signout", record.get('id'))
                if response.status_code == 200:
                    res_json = response.json()
                    if res_json.get("code") == "0":
                        print("签退成功")
                    else:
                        print("签退失败：", res_json.get("msg"))
                else:
                    print("请求失败，状态码：", response.status_code)
            else:
                print("已取消签到")
            break

    if not has_signable:
        print("当前没有检测到可签退的预约")

    input("按任意键返回...")

if __name__ == '__main__':
    main()