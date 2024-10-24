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
# print('''请选择操作选项:
#       1 查看用户账号信息
#       2 添加用户
#       3 删除用户
#       4 列出所有用户信息
#       0 退出''')

# for i in line:
#     command = input('请输入命令')
#     if command == 1:
#         print(members[1],[2],[3])
