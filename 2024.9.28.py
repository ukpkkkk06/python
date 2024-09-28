# a = float(input("请输入今日温度（单位:摄氏度）："))
# b = float(input("请输入今日气压(单位：帕): "))
# if a > 30 or a < -8:
#     print("不舒适")
# elif b > 300 or b < 20:
#     print("不舒适")
# elif 25 < a <= 30 and 200 < b <= 300:
#     print("比较舒适")
# elif 10 < a <=25 and 100 < b <= 200:
#     print("特别舒适")
# elif -8 <= a <= 10 and 20 <= b <= 100:
#     print("比较舒适")
# else:
#     print("本程序不能判断")
    
# high = float(input("请输入你的身高(单位米):"))
# weight = float(input("请输入你的体重(单位公斤):"))  
# age = int(input("请输入你的年龄:"))
# if age < 10:
#     print("小孩子去玩原神")
# elif age >= 60:
#     print("爆金币了老登")
# elif weight/high ** 2  > 24:
#     print("肥猪吧大概")
# elif weight/high ** 2 < 18:
#     print("骷髅兵吧大概")
# else:
#     print("哦哦还有这种正常人")

# var1 = [ 33, ['我的名字', 'test'], 'hello world!']
# var1.append('你好')
# print(var1)

# var1 = [ 33, ['我的名字', 'test'], 'hello world!']
# var1.insert(0,'你好')
# print(var1)

# var1 = [ 33, ['我的名字', 'test'], 'hello world!']
# var1.insert(1,'你好')
# print(var1)

# str1 = '大家好，我的名字叫：说的道理'
# a = str1.find('说的道理')
# print(a)

# str1 = '大家好，我的名字叫:东海帝皇'
# a = (str1.split(':') [1])
# print(a)

# sex = str(input('输入您的性别:'))
# high = float(input('请输入您的身高（厘米）：'))
# weight = float(input('请输入您的体重（公斤）：'))
# man_wei = (high-100) * 0.9
# women_wei = ((high-100)*0.9)-2.5
# if sex == '男':
#     if (man_wei - 5 ) <= weight <= (man_wei + 5): 
#         print("体重正常")
#     elif weight >  man_wei + 5:
#         print("体重高于标准")
#     else:
#         print("体重低于标准")
        
# else:
#     if (women_wei - 5 ) <= weight <= (women_wei + 5): 
#         print("体重正常")
#     elif weight >  women_wei + 5:
#         print("体重高于标准")
#     else:
#         print("体重低于标准")
# 正确做法↓
# gender = input('请输入您的性别：')
# gender = gender.replace(' ','')

# height = input('请输入您的身高（厘米）：')
# height = height.replace(' ','')
# height = height.replace('厘米','')
# height = int(height)

# weight = input('请输入您的体重（公斤）：')
# weight = weight.replace(' ','')
# weight = weight.replace('公斤','')
# weight = int(weight)

# if gender == '男':
#     standard = (height-100) * 0.9
# else:
#     standard = (height-100) * 0.9 - 2.5

# if standard - 5  < weight < standard + 5 :
#     print('体重健康')
# elif standard < weight:
#     print('太重了')
# else:
#     print('太轻了')

# str1 = '大家好，我的名字叫：'
# str2 = 'ukpkkkk'
# print(str1 + str2)

# name = str(input("请输入你的名字："))
# age = int(input("请输入你的年龄"))
# print(f'你的名字是:{name},你的年龄是:{age}')

# info = [
#     ['user1', 345.6, 12, '黄金'],
#     ['user2', 2345.6, 8, '白银'],
#     ['user3555', 55345.6, 12, '钻石'],
# ]
# print(f'用户:{info[0][0]:>10},积分:{info[0][1]:>10},等级:{info[0][2]:>3},头衔:{info[0][3]:>3}')
# print(f'用户:{info[1][0]:>10},积分:{info[1][1]:>10},等级:{info[1][2]:>3},头衔:{info[1][3]:>3}')
# print(f'用户:{info[2][0]:>10},积分:{info[2][1]:>10},等级:{info[2][2]:>3},头衔:{info[2][3]:>3}')
