def main():
    # 座位预约

    import os
    from src.core.Booking import book_seat
    from src.core.time_validation import time_input
    from src.core.IDConversion import get_id_by_space_name, get_floor_by_space_name

    os.system('cls' if os.name == 'nt' else 'clear')

    with open("token.txt", "r", encoding="utf-8") as f:
        token = f.read().strip()

    print("座位预约")
    print("——————————————————————————————————————————————")
    print("   [1]   常规预约")
    print("   [2]   同座多时段预约")
    print("   [3]   自动选择最佳座位（施工中）")
    choice = input("\n请输入你的选择: ")

    if choice == "1":
        date, begin, end = time_input(True)

        while True:
            space_name = input("请输入座位号: ")
            id = get_id_by_space_name(space_name)
            
            if id == "network error":
                print("网络错误，或许你要摸摸蓝色小猫了喵~")
                break
            elif id:
                break
            else:
                print("笨蛋！有这个座位号吗？")

        os.system('cls' if os.name == 'nt' else 'clear')
        print("常规预约")
        print("——————————————————————————————————————————————")
        
        response = book_seat(date, begin, end, id, token)

        if response.json().get('msg') == "成功":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("预约成功了喵~")
            print("————————————————————————")
            print(f"座位: {get_floor_by_space_name(space_name)}F {space_name.zfill(3)}")
            print(f"时间: {date} {begin}-{end}\n")

            print("请记得要去签到喵~")
            input("\n按任意键返回...")
        else:
            print(f"预约失败: {response.json().get('msg')}")
    elif choice == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("同座多时段预约")
        print("——————————————————————————————————————————————")

        while True:
            time_slot_count = input("请输入时间段段数：")
            if time_slot_count.isdigit() and int(time_slot_count) > 0 and int(time_slot_count) < 4:
                break
            else:
                print("时间段数应小于4，请重新输入")
        
        while True:
                space_name = input("请输入座位号: ")
                id = get_id_by_space_name(space_name)
                
                if id == "network error":
                    print("网络错误，或许你要摸摸蓝色小猫了")
                    break
                elif id:
                    break
                else:
                    print("笨蛋！有这个座位号吗？")

        date = [None] * int(time_slot_count)
        begin = [None] * int(time_slot_count)
        end = [None] * int(time_slot_count)

        for i in range(int(time_slot_count)):
            print(f"\n第 {i+1} 段")
            date[i], begin[i], end[i] = time_input(False)

        os.system('cls' if os.name == 'nt' else 'clear')
        print("预约情况")
        print("——————————————————————————————————————————————")
            
        for i in range(int(time_slot_count)):
            response = book_seat(date[i], begin[i], end[i], id, token)
            
            if response.json().get('msg') == "成功":
                print(f"第 {i+1} 段：预约成功")
                print("————————————————————————")
                print(f"座位: {get_floor_by_space_name(space_name)}F {space_name.zfill(3)}")
                print(f"时间: {date[i]} {begin[i]}-{end[i]}\n")
            else:
                print(f"预约失败: {response.json().get('msg')}")
        
        print("请记得要去签到喵~")
        input("\n按任意键返回...")
    elif choice == "3":
        print("此功能正在施工中，敬请期待。")

if __name__ == '__main__':
    main()