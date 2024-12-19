# import random   # 导入随机模块

# class RockPaperScissors:
#       def __init__(self):
#             # 手势列表：0 -> 石头, 1 -> 剪刀, 2 -> 布
#             self.options = ["石头", "剪刀", "布"]

#       def get_computer_choice(self):
#             # 随机生成计算机的手势
#             return random.choice(self.options)

#       def get_player_choice(self):
#             # 获取玩家输入并检查是否合法
#             print("请输入你的选择：0: 石头, 1: 剪刀, 2: 布")
#             choice = input("你的选择（输入数字）：")
#             while not choice.isdigit() or int(choice) not in range(3):
#                   print("输入无效，请重新输入")
#                   choice = input("你的选择（输入数字）：")
#             return self.options[int(choice)]

#       def decide_winner(self, player, computer):
#             # 判断胜负规则
#             print(f"你选择了：{player}")
#             print(f"计算机选择了：{computer}")
#             if player == computer:
#                   return "平局"
#             elif (player == "石头" and computer == "剪刀") or \
#                    (player == "剪刀" and computer == "布") or \
#                    (player == "布" and computer == "石头"):
#                   return "玩家赢"
#             else:
#                   return "计算机赢"

#       def play(self):
#             # 主游戏逻辑
#             print("欢迎来到人机猜拳游戏！")
#             while True:
#                   player_choice = self.get_player_choice()
#                   computer_choice = self.get_computer_choice()
#                   result = self.decide_winner(player_choice, computer_choice)
#                   print(f"结果：{result}")
#                   replay = input("是否继续游戏？(y/n): ")
#                   if replay.lower() != 'y':
#                         print("感谢你的参与，再见！")
#                         break

# # 主程序入口
# if __name__ == "__main__":
#       game = RockPaperScissors()
#       game.play()

import random

# 生成六位数字验证码
def generate_verification_code():
    code = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return code

# 调用函数生成验证码
verification_code = generate_verification_code()
print(f"生成的验证码是: {verification_code}")


import random

# 生成银行卡号，每四位用“-”分隔
def generate_bank_card(prefix, card_count):
    card_numbers = set()  # 用于保存不重复的卡号
    while len(card_numbers) < card_count:
        # 生成卡号的后10位
        suffix = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        card_number = f"{prefix}{suffix[:4]}{suffix[4:8]}{suffix[8:]}"
        # 格式化为每四位分隔
        card_number_formatted = f"{card_number[:4]}-{card_number[4:8]}-{card_number[8:12]}-{card_number[12:]}"
        card_numbers.add(card_number_formatted)
    return card_numbers

# 生成6位密码
def generate_password():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

# 为每种银行卡生成卡号和密码
def generate_bank_data():
    bank_data = {
        'A银行': {'prefix': '622525', 'count': 100},
        'B银行': {'prefix': '622538', 'count': 150},
        'C银行': {'prefix': '622575', 'count': 80},
    }
    
    for bank, data in bank_data.items():
        print(f"{bank} 的银行卡号和密码:")
        card_numbers = generate_bank_card(data['prefix'], data['count'])
        for card_number in card_numbers:
            password = generate_password()
            print(f"卡号: {card_number}, 密码: {password}")
        print("\n")

# 生成并打印数据
generate_bank_data()

class Book:
    def __init__(self, name, author, isbn, publisher, price):
        # 初始化书本的基本属性
        self.name = name
        self.author = author
        self.isbn = isbn
        self.publisher = publisher
        self.price = price

    def info(self):
        # 输出书的基本信息
        print(f"书名: {self.name}")
        print(f"作者: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"出版社: {self.publisher}")
        print(f"价格: {self.price}元")

# 实例化一个Book对象 book1
book1 = Book(
    name="Python编程入门",
    author="张三",
    isbn="978-7-111-12345-6",
    publisher="人民邮电出版社",
    price=49.8
)

# 调用 info() 方法，输出书的基本信息
book1.info()

class Square:
    def __init__(self, side):
        # 初始化正方形的边长
        self.side = side

    def get_perimeter(self):
        # 计算正方形的周长，周长 = 4 * 边长
        return 4 * self.side

    def get_area(self):
        # 计算正方形的面积，面积 = 边长 * 边长
        return self.side ** 2

# 创建Square类的对象，假设正方形的边长为5
square = Square(side=5)

# 调用方法计算周长和面积
perimeter = square.get_perimeter()
area = square.get_area()

# 输出结果
print(f"正方形的边长是: {square.side}")
print(f"正方形的周长是: {perimeter}")
print(f"正方形的面积是: {area}")

import math  # 引入math模块来使用π

class Circle:
    def __init__(self, r):
        # 初始化圆的半径
        self.r = r

    def getPerimeter(self):
        # 计算圆的周长，周长 = 2 * π * r
        return 2 * math.pi * self.r

    def getArea(self):
        # 计算圆的面积，面积 = π * r^2
        return math.pi * (self.r ** 2)

# 实例化一个Circle对象，假设半径为10
circle = Circle(r=10)

# 调用方法计算周长和面积
perimeter = circle.getPerimeter()
area = circle.getArea()

# 输出结果
print(f"圆的半径是: {circle.r}")
print(f"圆的周长是: {perimeter:.2f}")
print(f"圆的面积是: {area:.2f}")

class Employee:
    def __init__(self, name, gender, years_of_service, base_salary, post_allowance, performance_salary):
        # 初始化员工的基本信息和工资相关的属性
        self.name = name
        self.gender = gender
        self.years_of_service = years_of_service
        self.base_salary = base_salary
        self.post_allowance = post_allowance
        self.performance_salary = performance_salary

    def get_total_salary(self):
        # 计算应付工资：基础工资 + 岗位津贴 + 效益工资
        return self.base_salary + self.post_allowance + self.performance_salary

    def get_personal_tax(self):
        # 计算个人所得税：3500元以下免税，超出部分按3%计算
        total_salary = self.get_total_salary()
        if total_salary <= 3500:
            return 0
        else:
            return (total_salary - 3500) * 0.03

    def get_actual_salary(self):
        # 计算实发工资：应付工资 - 个人所得税
        total_salary = self.get_total_salary()
        personal_tax = self.get_personal_tax()
        return total_salary - personal_tax

    def display_info(self):
        # 输出员工的姓名、性别、工龄、应付工资和实发工资
        total_salary = self.get_total_salary()
        actual_salary = self.get_actual_salary()
        print(f"员工姓名: {self.name}")
        print(f"性别: {self.gender}")
        print(f"工龄: {self.years_of_service}年")
        print(f"应付工资: {total_salary}元")
        print(f"实发工资: {actual_salary}元")

# 创建员工对象并输出信息
employee1 = Employee(
    name="张伟",
    gender="男",
    years_of_service=5,
    base_salary=5000,
    post_allowance=800,
    performance_salary=1200
)

employee1.display_info()


class Student:
    # 类属性：学校、姓名、年龄
    schoolname = "未知学校"
    name = "未知姓名"
    age = 0

    def __init__(self, name, age):
        # 实例属性：通过构造方法传入姓名和年龄
        self.name = name
        self.age = age

    def introduce(self):
        # 返回学生的属性信息
        return f"学校: {Student.schoolname}, 姓名: {self.name}, 年龄: {self.age}"

class Undergraduate(Student):
    # 子类本科生增加学位属性
    def __init__(self, name, age, degree):
        # 通过构造方法初始化父类属性并设置degree属性
        super().__init__(name, age)
        self.degree = degree

    def introduce(self):
        # 重写父类的introduce方法，返回本科生的四个属性信息
        return f"学校: {Student.schoolname}, 姓名: {self.name}, 年龄: {self.age}, 学位: {self.degree}"

# 设置类属性的值
Student.schoolname = "清华大学"

# 创建Student对象并调用introduce()
student1 = Student(name="李雷", age=20)
print(student1.introduce())

# 创建Undergraduate对象并调用introduce()
undergrad1 = Undergraduate(name="韩梅梅", age=21, degree="学士")
print(undergrad1.introduce())


import math

# 父类：图形
class Shape:
    def getArea(self):
        pass

    def getLen(self):
        pass

# 矩形类（子类）
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        # 矩形的面积 = 宽度 * 高度
        return self.width * self.height

    def getLen(self):
        # 矩形的周长 = 2 * (宽度 + 高度)
        return 2 * (self.width + self.height)

    def __str__(self):
        # 返回矩形的基本信息
        return f"矩形: 宽度 = {self.width}, 高度 = {self.height}"

# 圆类（子类）
class Circle(Shape):
    def __init__(self, center, radius):
        self.center = center  # 圆心坐标
        self.radius = radius  # 半径

    def getArea(self):
        # 圆的面积 = π * 半径^2
        return math.pi * (self.radius ** 2)

    def getLen(self):
        # 圆的周长 = 2 * π * 半径
        return 2 * math.pi * self.radius

    def __str__(self):
        # 返回圆的基本信息
        return f"圆: 圆心 = {self.center}, 半径 = {self.radius}"

# 多态实现：根据传入的对象计算面积和周长
def print_area_and_len(shape):
    print(f"{shape.__str__()} 的面积: {shape.getArea()}，周长: {shape.getLen()}")

# 测试代码
# 创建矩形对象
rect = Rectangle(5, 3)

# 创建圆对象
circle = Circle((0, 0), 4)

# 调用多态方法，输出面积和周长
print_area_and_len(rect)
print_area_and_len(circle)
