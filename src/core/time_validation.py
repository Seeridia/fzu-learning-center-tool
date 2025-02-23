import datetime 

def time_input(check_interval: bool):
    """
    输入日期或偏移天数，验证日期合法性
    Args:
        check_interval: 是否验证时间区间不大于4.5小时
    Returns: 
        tuple: (datetime.date, str, str) - 日期, 开始时间, 结束时间
    """
    while True:
        try:
            user_input = input(f"请输入日期 (例如: {datetime.date.today()}) 或偏移天数（直接回车表示当天，1 表示明天）：")
            if "-" in user_input:
                parsed_date = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
            else:
                offset = int(user_input.strip()) if user_input.strip() != "" else 0
                parsed_date = datetime.date.today() + datetime.timedelta(days=offset)
            
            if parsed_date < datetime.date.today():
                raise ValueError("你难道想穿越到过去吗？")
            break
        except ValueError as e:
            print(f"错误: {str(e)}\n请重新输入")
            
    if check_interval:
        # 当需要验证时间区间不大于4.5小时时
        while True:
            # 开始时间输入和验证
            while True:
                try:
                    begin_input = input("请输入开始时间 (例如: 8 或 8.5): ")
                    begin_val = validate_time_input(begin_input, "开始时间")
                    if begin_val < 8:
                        raise ValueError("啊啦，喵喵还在睡觉呢，每天的开始时间不得早于8点")
                    if parsed_date == datetime.date.today():
                        now = datetime.datetime.now()
                        current_decimal = now.hour + now.minute / 60
                        if begin_val < current_decimal:
                            raise ValueError(f"笨死啦。现在都几点啦，还想约{begin_input}点的座位？")
                    break
                except ValueError as e:
                    print(f"错误: {str(e)}\n请重新输入")
            
            # 结束时间输入和验证
            while True:
                try:
                    end_input = input("请输入结束时间 (例如: 22 或 22.5): ")
                    end_val = validate_time_input(end_input, "结束时间")
                    if end_val > 22.5:
                        raise ValueError("喵喵也要休息了，每天的结束时间不得晚于22.5")
                    if end_val <= begin_val:
                        raise ValueError("笨死啦。你想约的座位时间是倒着的吗？")
                    break
                except ValueError as e:
                    print(f"错误: {str(e)}\n请重新输入")
                    
            # 验证输入的区间是否大于4.5小时
            if (end_val - begin_val) > 4.5:
                print("喵喵只能最多陪你学习 4.5 小时（；´д｀）ゞ")
                continue
            else:
                break
    else:
        # 原有逻辑：分别输入开始时间和结束时间
        # 开始时间输入和验证
        while True:
            try:
                begin_input = input("请输入开始时间 (例如: 8 或 8.5): ")
                begin_val = validate_time_input(begin_input, "开始时间")
                if begin_val < 8:
                    raise ValueError("啊啦，喵喵还在睡觉呢，每天的开始时间不得早于8点")
                if parsed_date == datetime.date.today():
                    now = datetime.datetime.now()
                    current_decimal = now.hour + now.minute / 60
                    if begin_val < current_decimal:
                        raise ValueError(f"笨死啦。现在都几点啦，还想约{begin_input}点的座位？")
                break
            except ValueError as e:
                print(f"错误: {str(e)}\n请重新输入")
        
        # 结束时间输入和验证
        while True:
            try:
                end_input = input("请输入结束时间 (例如: 22 或 22.5): ")
                end_val = validate_time_input(end_input, "结束时间")
                if end_val > 22.5:
                    raise ValueError("喵喵也要休息了，每天的结束时间不得晚于22.5")
                if end_val <= begin_val:
                    raise ValueError("笨死啦。你想约的时间是倒着的吗？")
                break
            except ValueError as e:
                print(f"错误: {str(e)}\n请重新输入")

    begin_hour = convert_hour_input(begin_val)
    end_hour = convert_hour_input(end_val)
    return parsed_date, begin_hour, end_hour

def validate_time_input(time_str, label):
    if "." in time_str:
        parts = time_str.split(".")
        if len(parts) != 2 or parts[1] != "5":
            raise ValueError(f"{label}不合法，小数部分只能为5")
    return float(time_str)

def convert_hour_input(time_value):
    hour_int = int(time_value)
    minutes = "30" if (time_value - hour_int) >= 0.5 else "00"
    return f"{hour_int:02d}:{minutes}"