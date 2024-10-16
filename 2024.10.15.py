# def test(number):
#     str_num = str(number) 
#     if len(str_num) != 5:
#         return False
#     reversed_num = str_num[::-1]
#     return str_num == reversed_num
# user_input = int(input('请输入一个五位数')) 
# try:
#     number = int(user_input)
#     if test(number):
#         print(f"{number}是一个回文数")
#     else:
#         print(f"{number}不是一个回文数")
# except ValueError:
#     print("输入无效")

# user_input = input("请输入一个字符串")
# alpha = 0
# digit = 0 
# space = 0
# other = 0
# for i in user_input:
#     if i.isalpha():
#         alpha+=1
#     elif i.isspace():
#         space+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         other+=1
# print(f'字母个数为{alpha}空格字数{space},数字字数为{digit},其他个数为{other}')

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# prime_numbers = []
# for number in range(101, 201):
#     if is_prime(number):
#         prime_numbers.append(number)

# print("101到200之间有", len(prime_numbers), "个素数")
# print("这些素数分别是：", prime_numbers)

# test =  0 
# for i in range(0,101):
#     if i %2 == 0:
#         test = test + i
# print(test)

# user = 'root'
# passwd = 'westos'
# user_login = 0

# while user_login < 3:
#     user_input = input('请输入用户名')
#     passwd_input = input('请输入密码')
#     if user_input == user and passwd_input == passwd:
#         print('登陆成功')
#     else:
#         user_login+=1
#         print('登录失败')

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {j * i}", end="\t")
#         j += 1
#     print()
#     i += 1

# for i in range(0,101):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i) 

# def fibonacci_sequence(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         a, b = 0, 1
#         for _ in range(2, n + 1):
#             a, b = b, a + b
#         return b

# def sum_of_sequence(n):
#     sum_seq = 0
#     for i in range(1, n + 1):
#         numerator = fibonacci_sequence(i + 1)
#         denominator = fibonacci_sequence(i)
#         sum_seq += numerator / denominator
#     return sum_seq

# result = sum_of_sequence(20)
# print("The sum of the first 20 terms of the sequence is:", result)


# def find_narcissistic_numbers():
#     for num in range(100, 1000):
#         # 分解出百位、十位和个位数字
#         hundreds = num // 100
#         tens = (num % 100) // 10
#         ones = num % 10
        
#         # 计算各位数字的立方和
#         sum_of_cubes = hundreds ** 3 + tens ** 3 + ones ** 3
        
#         # 判断是否为水仙花数
#         if sum_of_cubes == num:
#             print(num)

# find_narcissistic_numbers()
