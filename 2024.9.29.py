# str1 = '''
# 熊宁
# 杰益

# 王伟伟

# 青芳

# 玉琴
# 焦候涛
# 莫福
# 杨高旺
# 唐欢欢
# 韩旭
# '''

# str2 = '''
# 焦候涛 
# 熊宁 
# 玉琴 

# 骆龙 

# 韩旭 
# 杨高旺

# 杰益  

# 莫福  

# 伟伟

# 李福  
# '''

# # 注意：有的人名 可能是另外一个人名的一部分，
# # 比如 伟伟 是王伟伟 的一部分， 
# # 所以我们不能 通过 'name in str1' 这样的方式判断


# # 先定义一个函数，可以把参数字符串中的人名都放入一个列表中

# def getNameList(namesStr):
#     tmp = namesStr.splitlines()

#     # 去掉其中的空行和人名前后的空格
#     names = []
#     for name in tmp:
#         name = name.strip()
#         if name == '':
#             continue

#         names.append(name)

#     return names


# names1 = getNameList(str1)
# names2 = getNameList(str2)

# print('str1中独有的人名是：')
# for name in names1:
#     if name not in names2:
#         print(name)

# print('\n\n')

# print('str2中独有的人名是：')
# for name in names2:
#     if name not in names1:
#         print(name)
# 正确答案↑