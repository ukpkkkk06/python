# a = 0 
# for a in range(1,101):
#     a += 1
# print(a)

# buy_cost = float(input("请输入你的购买金额"))
# if buy_cost > 50 and buy_cost < 100:
#     buy_cost = buy_cost * 0.9
#     print("给你九折优惠","请支付:",buy_cost)
# elif buy_cost > 100:
#     buy_cost = buy_cost * 0.8
#     print("给您八折优惠","请您支付:",buy_cost)
# else :
#     print("穷逼别来买东西，没折扣","给钱:",buy_cost)

# year = float(input("请输入当前年份(公元纪年)"))
# if year % 4 == 0 and year % 100 != 0:
#     print("普通闰年")
# elif year % 400 == 0:
#     print("世纪闰年")
# else:
#     print("不是闰年")
    
# month = input("请输入年份和月份(XXXX XX)")
# year = int(month.split(' ')[0])
# month2 = int(month.split(' ')[1])
# if month2 in [1,3,5,7,8,10,12]:
#     print("本月31天")
# elif month2 in [4,6,9,11]:
#     print("本月30天")
# elif year % 4 == 0:
#     print("本月29天")
# else :
#     print("本月28天")

# def login(user,passwd):
#     if user == 'admin' and passwd == 123456:
#         print("登陆成功")    
#     elif user == 'xiaoming' and passwd == 123:
#         print("登陆成功")
#     else:
#         print("登陆失败")
        
# login_us = input("请输入用户名")
# login_pss = float(input("请输入密码"))
# login(login_us,login_pss)

# import math
# def Formula(a,b,c):
#     equation = b**2 - 4*a*c
#     if equation == 0:
#         print("有两个相同实根")
#         real_root = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
#         real_root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
#         print(real_root,real_root2)
#     elif equation > 0:
#         print("有两个不等实根")
#         real_root = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
#         real_root2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
#         print(real_root,real_root2)
#     else:
#         print("无实数根")
    

# coefficient_a = float(input("请输入a(a≠0): "))
# coefficient_b = float(input("请输入b: "))
# coefficient_c = float(input("请输入c: "))
# Formula(coefficient_a,coefficient_b,coefficient_c)
