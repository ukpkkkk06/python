# import time

# # 输入高考时间
# gaokao_date = input("请输入高考日期（格式为YYYY-MM-DD）：")
# try:
#     # 将输入的高考时间转换为时间戳
#     gaokao_time_struct = time.strptime(gaokao_date, "%Y-%m-%d")
#     gaokao_timestamp = time.mktime(gaokao_time_struct)

#     # 获取当前时间的时间戳
#     current_timestamp = time.time()

#     # 计算剩余天数
#     remaining_seconds = gaokao_timestamp - current_timestamp
#     remaining_days = int(remaining_seconds // (24 * 3600))

#     # 输出结果
#     print("===============================")
#     print(f"高考时间是 {gaokao_date}")
#     print(f"今天是 {time.strftime('%Y-%m-%d')}")
#     if remaining_days >= 0:
#         print(f"距离高考还有 {remaining_days} 天")
#     else:
#         print("高考已经结束！")
#     print("===============================")
# except ValueError:
#     print("日期格式不正确，请输入 YYYY-MM-DD 格式的日期！")

# import time

# # 获取当前时间
# current_time = time.localtime()

# # 使用 time.strftime() 格式化当前日期和时间
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

# # 输出结果
# print("当前日期和时间为：")
# print(formatted_time)

# import time

# # 用户输入倒计时时间（单位：秒）
# try:
#     countdown_time = int(input("请输入倒计时时间（秒）："))

#     # 倒计时
#     while countdown_time > 0:
#         print(f"倒计时：{countdown_time} 秒", end="\r")
#         time.sleep(1)
#         countdown_time -= 1

#     # 倒计时结束提示
#     print("时间到！")
# except ValueError:
#     print("请输入一个有效的整数！")

from datetime import datetime

# 输入身份证号码（假设为18位）
id_number = input("请输入身份证号码（18位）：").strip()

# 校验身份证号码是否合法
if len(id_number) != 18 or not id_number[:-1].isdigit():
    print("身份证号码不合法，请输入正确的18位号码！")
else:
    # 提取出生年月日
    birth_year = int(id_number[6:10])
    birth_month = int(id_number[10:12])
    birth_day = int(id_number[12:14])

    # 获取当前日期
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day

    # 计算年龄
    age = current_year - birth_year

    # 判断是否成年
    if age > 18:
        print("成年人")
    elif age < 18:
        print("未成年人")
    else:  # 如果年龄正好等于18岁，进一步判断
        if current_month > birth_month:
            print("成年人")
        elif current_month < birth_month:
            print("未成年人")
        else:  # 如果月份相同，进一步判断日期
            if current_day >= birth_day:
                print("成年人")
            else:
                print("未成年人")
