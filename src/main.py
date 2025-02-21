import os

os.system('cls' if os.name == 'nt' else 'clear')

if os.path.exists("token.txt"):
    with open("token.txt", "r", encoding="utf-8") as f:
        token_input = f.read().strip()
else:
    token_input = input("请输入你的token: ")
    with open("token.txt", "w", encoding="utf-8") as f:
        f.write(token_input)
        print("token 已保存\n")

while True:
    
    print("FZU 学习中心预约")
    print("——————————————————————————————")

    print("   [1]   座位情况")
    print("   [2]   预约座位")
    print("   [3]   取消预约")
    print("   [4]   预约记录")
    print("   [5]   退出")
    choice = input("\n请输入你的选择: ")
    if choice == "1":
        os.system("python src/seat.py")
    elif choice == "2":
        os.system("python src/book.py")
    elif choice == "3":
        os.system("python src/cancel.py")
    elif choice == "4":
        os.system("python src/record.py")
    elif choice == "5":
        break
    else:
        print("输入错误，请重新输入")
    print("——————————————————————————————————————————————")