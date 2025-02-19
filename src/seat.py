import os
import datetime
from core.query import query_seat_status

os.system('cls' if os.name == 'nt' else 'clear')

with open("token.txt", "r", encoding="utf-8") as f:
        token_input = f.read().strip()

print("座位预约情况")
print("——————————————————————————————————————————————")

# 日期输入和验证
while True:
    try:
        user_input = input(f"请输入日期 (例如: {datetime.date.today()}) 或偏移天数（直接回车或输入 0 表示当天，1 表示明天）：")
        if "-" in user_input:
            parsed_date = datetime.datetime.strptime(user_input, "%Y-%m-%d").date()
        else:
            offset = int(user_input.strip()) if user_input.strip() != "" else 0
            parsed_date = datetime.date.today() + datetime.timedelta(days=offset)
        
        if parsed_date < datetime.date.today():
            raise ValueError("输入的日期不得是今天之前的日期")
        break
    except ValueError as e:
        print(f"错误: {str(e)}\n请重新输入")

def validate_time_input(time_str, label):
    if "." in time_str:
        parts = time_str.split(".")
        if len(parts) != 2 or parts[1] != "5":
            raise ValueError(f"{label}不合法，小数部分只能为5")
    return float(time_str)

# 开始时间输入和验证
while True:
    try:
        begin_input = input("请输入开始时间小时数 (例如: 8 或 8.5): ")
        begin_val = validate_time_input(begin_input, "开始时间")
        if begin_val < 8:
            raise ValueError("每天的开始时间不得早于8点")
        if parsed_date == datetime.date.today():
            now = datetime.datetime.now()
            current_decimal = now.hour + now.minute / 60
            if begin_val < current_decimal:
                raise ValueError("当天的开始时间不得早于当前的时间")
        break
    except ValueError as e:
        print(f"错误: {str(e)}\n请重新输入")

# 结束时间输入和验证
while True:
    try:
        end_input = input("请输入结束时间小时数 (例如: 22 或 22.5): ")
        end_val = validate_time_input(end_input, "结束时间")
        if end_val > 22.5:
            raise ValueError("每天的结束时间不得晚于22.5")
        if end_val <= begin_val:
            raise ValueError("结束时间必须晚于开始时间")
        break
    except ValueError as e:
        print(f"错误: {str(e)}\n请重新输入")

def convert_hour_input(time_value):
    hour_int = int(time_value)
    minutes = "30" if (time_value - hour_int) >= 0.5 else "00"
    return f"{hour_int:02d}:{minutes}"

begin_hour = convert_hour_input(begin_val)
end_hour = convert_hour_input(end_val)

# 调用查询模块函数执行座位查询
query_seat_status(parsed_date, begin_hour, end_hour, token_input)
