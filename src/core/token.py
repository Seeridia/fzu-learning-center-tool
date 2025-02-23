def token_get():
    print(
        " *     FZU-learning-center-tool     /     Author - Seeridia\n"
        " *     https://github.com/Seeridia/fzu-learning-center-tool\n"
        " *     \n"
        " *     Version - 0.1.0"
    )
    print("\n请勿滥用，本项目仅用于学习和测试！\n")
    print("运行该程序需要获取 token")
    print('请访问 https://aiot.fzu.edu.cn/api/ibs 完成登录后，复制网址中 "token=" 后的内容')

    while True:
        token_input = input("\n> token = ")

        if not token_input:
            print("Token 不能为空")
            continue

        if not (len(token_input) == 36 and token_input.count('-') == 4):
            print("Token 格式错误，请输入正确的 token")
            continue

        try:
            parts = token_input.split('-')
            if len(parts) != 5 or not all(len(p) in [8, 4, 4, 4, 12] for p in parts):
                raise ValueError
        except:
            print("Token 格式错误，请输入正确的 token")
            continue

        with open("token.txt", "w", encoding="utf-8") as f:
            f.write(token_input)
            print("token 已保存\n")
        break
