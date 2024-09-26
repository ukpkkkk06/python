# total = float(input("请输入总收入: "))
# cost_w = float(input("请输入工资: "))
# cost_e = float(input("请输入餐饮费: "))
# cost_t = float(input("请输入交通费"))
# profit = (total-cost_w-cost_e-cost_t)*0.8
# print("你的总利润为:",str(profit))

# def printlen():
#     a = input("请输入一个字符串：")
#     lenghth = len(a)
#     print("长度为",lenghth)
# printlen()

# def is_palindrome(number):
#     # 将数字转换为字符串以便操作
#     str_num = str(number)
#     # 检查字符串长度是否为4位
#     if len(str_num) != 4:
#         return False
#     # 反转字符串
#     reversed_num = str_num[::-1]
#     # 比较原始数字和反转后的数字
#     return str_num == reversed_num

# # 获取用户输入
# user_input = input("请输入一个四位整数：")
# try:
#     # 尝试将输入转换为整数
#     number = int(user_input)
#     # 判断是否为回文数并输出结果
#     if is_palindrome(number):
#         print(f"{number} 是一个回文数。")
#     else:
#         print(f"{number} 不是一个回文数。")
# except ValueError:
#     print("输入无效，请输入一个四位整数。")

# a = float(input("请输入一个数: "))
# b = float(input("请输入一个数: "))
# c = float(input("请输入一个数: "))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)
        

# a = float(input("请输入一个数: "))
# b = float(input("请输入一个数: "))
# c = float(input("请输入一个数: "))
# if a>b:
#     if a>c:
#         print(a)
# else:
#     if a<c:
#         print(c)
#     else:
#             print(b)

# user_name=input("请输入用户名:" )
# passw=int(input("请输入密码: "))
# user_name_back="admin"
# user_password=123456
# if user_name == user_name_back and passw == user_password:
#     print("成功登陆")
# else:
#     print("用户名或密码错误")

# a = int(input("请输入一个整数："))
# if a > 0:
#     print("这是正数")
# else:
#     print("这是负数")

# score=int(input("请输入分数: "))
# if score > 100:
#     print("请输入正确数字")
# elif 90 <= score and score<=100:
#     print("A")
# elif 80<=score and score<90:
#     print("B")
# elif 70<=score and score<80:
#     print("C")
# elif 60<=score and score<70:
#     print("D")
# else:
#     print("不及格")

# def compute(weight,area):
#     first_weight_price = {
#         "01":12,
#         "02":13,
#         "03":14
#     }
#     ex_weight_price={
#         "01":2,
#         "02":3,
#         "03":3
#     }
#     first_weight=2
    
#     if weight<=first_weight:
#         price = first_weight_price[area]
#     else:
#         ex_weight = weight - first_weight
#         price = first_weight_price[area] + ex_weight_price[area] * ex_weight
#     return price 
# weight = float(input("请输入快递重量（kg）"))
# area = input("请输入区号(01-华北，02-华东，03-华北):")
# price = compute(weight,area)
# print("快递费用为",price)

# score = float(input("请输入分数"))
# if score < 0 or score >100:
#     print("成绩不合法")
# elif score>90:
#     print("A")
# elif score>80:
#     print("B")
# elif score>70:
#     print("C")
# elif score>60:
#     print("D")
# else:
#     print("E")
    
    
    
    