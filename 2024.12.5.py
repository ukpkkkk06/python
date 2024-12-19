P# def collatz_steps(n):
#     steps = 0
#     while n != 1:
#         if n % 2 == 0:  # 如果n是偶数
#             n = n // 2
#         else:  # 如果n是奇数
#             n = 3 * n + 1
#         steps += 1  # 计数器增加
#     return steps

# # 定义饮品信息
# def all_goods():
#     goods = {
#         "可口可乐": 2.5, "百事可乐": 2.5, "冰红茶": 3, "脉动": 3.5, "果缤纷": 3,
#         "绿茶": 3, "茉莉花茶": 3, "尖叫": 2.5
#     }
#     return goods

# # 展示饮品信息
# def show_goods():
#     goods = all_goods()
#     print("饮品信息：")
#     for drink, price in goods.items():
#         print(f"{drink}: {price:.2f}")
#     print("\n请输入您想要购买的饮品名称及数量（如：可口可乐 2），输入'q'退出。")

# # 计算总额
# def total(goods_dict):
#     total_price = 0
#     while True:
#         choice = input("请输入饮品名称及购买数量（如：可口可乐 2）：")
#         if choice.lower() == 'q':
#             break
#         try:
#             drink, quantity = choice.split()
#             quantity = int(quantity)
#             if drink in goods_dict:
#                 total_price += goods_dict[drink] * quantity
#                 print(f"您购买了 {quantity} 杯 {drink}，单价 ￥{goods_dict[drink]:.2f}，总价 ￥{goods_dict[drink] * quantity:.2f}")
#             else:
#                 print("该饮品不存在，请重新选择。")
#         except ValueError:
#             print("输入格式不正确，请按格式输入：饮品名称 数量")
#     return total_price

# # 主函数
# def main():
#     goods_dict = all_goods()
#     show_goods()  # 展示饮品信息
#     total_price = total(goods_dict)  # 计算总额
#     print(f"\n您的总消费为：￥{total_price:.2f}")

# # 调用主函数
# if __name__ == "__main__":
#     main()

# def rabbit_pairs(n):
#     # 递归终止条件：第一个月和第二个月都有 1 对兔子
#     if n == 1 or n == 2:
#         return 1
#     # 递归计算第n个月的兔子数量
#     return rabbit_pairs(n - 1) + rabbit_pairs(n - 2)

# # 用户输入月份，计算兔子数量
# n = int(input("请输入月份数："))
# total_rabbits = rabbit_pairs(n)
# print(f"{n}个月后共有 {total_rabbits} 对兔子")

# # 合并两个已排序的子序列
# def merge(left, right):
#     result = []
#     i = j = 0
    
#     # 合并两个已排序的子序列
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     # 如果左边子序列有剩余，直接加入结果
#     while i < len(left):
#         result.append(left[i])
#         i += 1

#     # 如果右边子序列有剩余，直接加入结果
#     while j < len(right):
#         result.append(right[j])
#         j += 1

#     return result

# # 递归实现归并排序
# def merge_sort(arr):
#     # 递归终止条件：如果数组长度为1或0，直接返回
#     if len(arr) <= 1:
#         return arr
    
#     # 拆分数组为两部分
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])  # 递归排序左部分
#     right = merge_sort(arr[mid:])  # 递归排序右部分
    
#     # 合并两部分并返回
#     return merge(left, right)

# # 测试归并排序
# if __name__ == "__main__":
#     arr = [8, 4, 5, 7, 1, 3, 6, 2]
#     print("原始数组:", arr)
#     sorted_arr = merge_sort(arr)
#     print("排序后的数组:", sorted_arr)

# 学生管理系统
class Student:
    def __init__(self):
        self.students = {}  # 用学号作为键，学生信息字典作为值
    
    # 添加学生信息
    def add_student(self):
        student_id = input("请输入学生学号：")
        if student_id in self.students:
            print("该学号已存在！")
            return
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        self.students[student_id] = {"name": name, "age": age}
        print(f"学生 {name} 添加成功！")
    
    # 删除学生信息
    def delete_student(self):
        student_id = input("请输入要删除的学生学号：")
        if student_id not in self.students:
            print("学号不存在！")
            return
        del self.students[student_id]
        print(f"学号为 {student_id} 的学生已删除！")
    
    # 修改学生信息
    def update_student(self):
        student_id = input("请输入要修改的学生学号：")
        if student_id not in self.students:
            print("学号不存在！")
            return
        name = input(f"请输入新的学生姓名（当前：{self.students[student_id]['name']}）：")
        age = input(f"请输入新的学生年龄（当前：{self.students[student_id]['age']}）：")
        self.students[student_id] = {"name": name, "age": age}
        print(f"学号为 {student_id} 的学生信息已更新！")
    
    # 查询学生信息
    def query_student(self):
        student_id = input("请输入要查询的学生学号：")
        if student_id not in self.students:
            print("学号不存在！")
            return
        student_info = self.students[student_id]
        print(f"学号：{student_id}，姓名：{student_info['name']}，年龄：{student_info['age']}")
    
    # 显示菜单
    def show_menu(self):
        print("\n学生管理系统")
        print("1. 添加学生")
        print("2. 删除学生")
        print("3. 修改学生")
        print("4. 查询学生")
        print("5. 退出系统")
    
    # 主程序
    def run(self):
        while True:
            self.show_menu()
            choice = input("请输入您的选择（1-5）：")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.delete_student()
            elif choice == "3":
                self.update_student()
            elif choice == "4":
                self.query_student()
            elif choice == "5":
                print("感谢使用学生管理系统！")
                break
            else:
                print("无效选择，请重新输入！")

# 创建学生管理系统实例并运行
if __name__ == "__main__":
    system = Student()
    system.run()
