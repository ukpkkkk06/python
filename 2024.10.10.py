# ageTable = '''
#     诸葛亮, 28
#     刘备, 48
#     刘琦, 25
#     赵云, 32
#     张飞, 43
#     关羽, 45
# '''
# agelist = []
# for item in ageTable.split('\n'):
#     if item.strip() == '':
#         continue
#     agelist.append(item)
# g30 = []
# l30 = []
# for oneman in agelist:
#     name,age = oneman.split(',')
#     age = int(age.strip())
#     name = name.strip()
#     if age >= 30:
#         g30.append(name)
#     else:
#         l30.append(name)
# print('大于等于30岁的人有:')
# for man in g30:
#     print(man)


# print('\n小于30岁的人有:')
# for man in l30:
#     print(man)

# def calculate_score(rounds):
#     guan_win_round = 0
#     zhang_win_round = 0
#     ping_round   = 0

#     # 取出列表里面每一局round，进行如下处理：
#     for round in rounds:
#         guan = round[0]
#         zhang = round[1]

#         # 判断谁赢
#         win = None
#         if guan == '剪刀':
#             if zhang == '石头':
#                 win = 'z'
#             elif zhang == '剪刀':
#                 win = '='
#             elif zhang == '布':
#                 win = 'g'
#         elif guan == '石头':
#             if zhang == '石头':
#                 win = '='
#             elif zhang == '剪刀':
#                 win = 'g'
#             elif zhang == '布':
#                 win = 'z'
#         elif guan == '布':
#             if zhang == '石头':
#                 win = 'g'
#             elif zhang == '剪刀':
#                 win = 'z'
#             elif zhang == '布':
#                 win = '='

#         if win == 'g':
#             print('关羽赢')
#             guan_win_round += 1
#         elif win == 'z':
#             print('张飞赢')
#             zhang_win_round += 1
#         elif win == '=':
#             print('平局')
#             ping_round  += 1

#     print('\n=============\n')
#     print(f'关羽赢{guan_win_round}次')
#     print(f'张飞赢{zhang_win_round}次')
#     print(f'平局{ping_round}次')

#     if guan_win_round> zhang_win_round:
#         print('关羽赢')
#     elif  guan_win_round < zhang_win_round:
#         print('张飞赢')
#     else:
#         print('平局')

# calculate_score([['剪刀', '石头'], ['布', '剪刀'], ['剪刀', '剪刀']])