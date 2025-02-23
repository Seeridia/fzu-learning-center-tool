#
#     FZU-learning-center-tool     /     Author - Seeridia
#     https://github.com/Seeridia/fzu-learning-center-tool
#     
#     Version - 0.1.0
#


import os
from src.core.token import token_get

if os.path.exists("token.txt"):
    with open("token.txt", "r", encoding="utf-8") as f:
        token_input = f.read().strip()
else:
    token_get()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("FZU 学习中心预约")
    print("——————————————————————————————")
    print("   [1]   座位情况")
    print("   [2]   预约座位")
    print("   [3]   取消预约")
    print("   [4]   预约记录")
    print("   [5]   签到")
    print("   [6]   签退")
    print("\n   [7]   退出")
    print("   [8]   修改 token")
    
    choice = input("\n请输入你的选择: ")
    if choice == "1":
        import src.seat
        src.seat.main()
    elif choice == "2":
        import src.book
        src.book.main()
    elif choice == "3":
        import src.cancel
        src.cancel.main()
    elif choice == "4":
        import src.record
        src.record.main()
    elif choice == "5":
        import src.sign
        src.sign.main()
    elif choice == "6":
        import src.sign_out
        src.sign_out.main()
    elif choice == "8":
        os.system('cls' if os.name == 'nt' else 'clear')
        token_get()
    elif choice == "7":
        break
    else:
        print("输入错误，请重新输入")
    print("——————————————————————————————————————————————")