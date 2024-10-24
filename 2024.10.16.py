# def calculate_score_by_surname(file_path):
#     # 创建一个字典来存储姓氏及其对应的积分总和
#     score_dict = {}

#     # 打开文件并逐行读取数据
#     with open(file_path, 'r', encoding='utf-8') as file:
#         for line in file:
#             # 去除行尾的换行符并按空格分割数据
#             data = line.strip().split()
#             # 提取姓氏（取第一个字符）
#             surname = data[0][0]
#             # 提取积分（转换为整数）
#             score = int(data[1])

#             # 如果姓氏已经在字典中，累加积分；否则，将姓氏添加到字典中并设置初始积分
#             if surname in score_dict:
#                 score_dict[surname] += score
#             else:
#                 score_dict[surname] = score

#     # 输出结果
#     for surname, total_score in score_dict.items():
#         print(f"{surname} : {total_score}")

# # 调用函数并传入文件路径
# calculate_score_by_surname('0016_1.txt')

# from pprint import pprint

# members = {
#     1 :{'name':'白月黑羽', 'level':3, 'coins':300},
#     2 :{'name':'短笛魔王', 'level':5, 'coins':330},
#     3 :{'name':'紫气一元', 'level':6, 'coins':340},
#     4 :{'name':'拜月主',   'level':3, 'coins':32200},
#     5 :{'name':'诸法空',   'level':4, 'coins':330},
#     6 :{'name':'暗光城主', 'level':3, 'coins':320},
#     7 :{'name':'心魔尊',   'level':3, 'coins':2300},
#     8 :{'name':'日月童子', 'level':8, 'coins':3450},
#     9 :{'name':'不死尸王', 'level':3, 'coins':324},
#     10:{'name':'天池剑尊', 'level':9, 'coins':13100},
# }


# # 因为要根据用户名查找用户信息，需要改变字典格式
# # 以用户名为key，创建一个字典

# name2info = {}
# for k,v in members.items():
#     name = v['name']
#     # 因为id也是要查询的内容，加到 字典的 value值中
#     v['id'] = k
#     name2info[name] = v


# # 定义查看用户账号的处理函数
# def checkAccount():
#     name = input('请输入查找的用户账号:')
#     if name not in name2info:
#         print(f'对不起，账号 {name} 不存在.')
#         return

#     info = name2info[name]
#     print(f'账号: {name} , ID : {info["id"]} , 等级：{info["level"]} , 金币：{info["coins"]} ')    


# # 定义添加用户账号的处理函数
# def addAccount():
#     while True:
#         name = input('请输入添加用户的账号:')
#         if name in name2info:
#             print('对不起，该账号已经存在')
#         else:
#             break

#     while True:
#         level = input('请输入该用户的等级:')
#         # 如果不是数字 ， 则输入格式错误
#         if not level.isdigit():
#             print('对不起，等级必须为一个数字')
#         else:
#             level = int(level) # 转化为整数
#             break


#     while True:
#         coins = input('请输入该用户的金币数量:')
#         # 如果不是数字 ， 则输入格式错误
#         if not coins.isdigit():
#             print('对不起，金币数 必须为一个数字')
#         else:
#             coins = int(coins) # 转化为整数
#             break

#     # 要产生一个不存在的ID号， 这里我们取 当前最大的ID号+ 1
#     newId = max(members.keys()) + 1
#     # 注意： 两个字典里面都要添加
#     members[newId] =  {'name':name, 'level':level, 'coins':coins}
#     name2info[name] = {'name':name, 'level':level, 'coins':coins, 'id':newId}


# # 定义删除用户账号的处理函数
# def delAccount():
#     name = input('请输入要删除的用户账号:')
#     if name not in name2info:
#         print(f'对不起，账号 {name} 不存在.')
#         return

#     # 注意： 两个字典里面都要删除
#     theID = name2info[name]['id']
#     name2info.pop(name)
#     members.pop(theID)


# # 定义打印表内容的处理函数
# def showTables():    
#     print('\n现在name2info的表内容是：\n')
#     pprint(name2info)
#     print('\n现在members的表内容是：\n')
#     pprint(members)



# menu = '''
# 请选择操作选项：
#    1 查看用户账号信息
#    2 添加用户
#    3 删除用户
#    4 列出所有用户信息
#    0 退出
# '''   
# # 显示主菜单
# while True:
#     choice = input(menu)

#     # 选择查看查看用户账号
#     if choice == '1':
#         checkAccount()
#     elif choice == '2':
#         addAccount()
#     elif choice == '3':
#         delAccount()
#     elif choice == '4':
#         showTables()
#     elif choice == '0':
#         break