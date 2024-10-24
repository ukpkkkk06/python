# # 获取用户基本信息
# name = input("请输入您的姓名：")
# position = input("请输入您的职位：")
# phone = input("请输入您的电话：")
# email = input("请输入您的邮箱：")

# # 插入用户基本信息到名片模板
# card_template = """
# -----------------------------------
# 姓名：{}
# 职位：{}
# 电话：{}
# 邮箱：{}
# -----------------------------------
# """
# formatted_card = card_template.format(name, position, phone, email)

# # 输出名片
# print(formatted_card)

# def convert_date_format(date_str):
#     # 使用split()方法按空格分割日期字符串
#     date_parts = date_str.split()

#     # 使用列表索引取出年、月、日
#     year = date_parts[0]
#     month = date_parts[1]
#     day = date_parts[2]

#     # 使用+运算符拼接新的日期格式
#     new_date_str = year + "年" + month + "月" + day + "日"

#     return new_date_str

# # 测试示例
# input_date = input("请输入时间")
# output_date = convert_date_format(input_date)
# print(output_date) 

# text = "我们拥有多年的品牌战略规划及标志设计、商标注册经验；专业提供公司标志设计与商标注册一条龙服务。我们拥有最优秀且具有远见卓识的设计师，使我们的策略分析严谨，设计充满创意。我们有信心为您缔造最优秀的品牌形象设计服务，将您的企业包装得更富价值。"
# target_word = "最优秀"
# replacement_word = "较优秀"

# # 使用find()方法查找目标词语
# position = text.find(target_word)

# # 如果找到了目标词语，使用replace()方法替换
# if position != -1:
#     text = text.replace(target_word, replacement_word)

# print(text)


# def check_bonus(attendance):
#     absences = attendance.count('A')
#     lates = attendance.count('L')
    
#     if absences == 0 and lates == 0:
#         return "可以拿到奖金"
#     elif absences == 0 and lates <= 2:
#         return "可以拿到奖金"
#     elif absences == 1 and lates <= 2:
#         return "不能拿到奖金"
#     elif absences == 2 and lates <= 2:
#         return "不能拿到奖金"
#     elif absences > 2:
#         return "不能拿到奖金"

# attendance = "PPPpPPPPLPPPPPPpPPPPPP"
# result = check_bonus(attendance)
# print(result)

# # 输入古诗信息
# title = input("请输入古诗标题：")
# author = input("请输入作者（包括朝代和姓名）：")
# poem_type = input("请输入古诗类型（四言诗、五言诗或七言诗）：")
# content = input("请输入古诗内容（包括标点符号和汉字）：")

# # 根据古诗类型确定每行字数
# if poem_type == "四言诗":
#     line_length = 5
# elif poem_type == "五言诗":
#     line_length = 6
# elif poem_type == "七言诗":
#     line_length = 8
# else:
#     print("无效的古诗类型")
#     exit()

# # 排版古诗
# print("\n" + title)
# print(author)
# for i in range(0, len(content), line_length):
#     print(content[i:i+line_length])



# def password_strength(password):
#     has_digit = False
#     has_lower = False
#     has_upper = False
#     has_special = False

#     special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

#     for char in password:
#         if char.isdecimal():
#             has_digit = True
#         elif char.islower():
#             has_lower = True
#         elif char.isupper():
#             has_upper = True
#         elif char in special_chars:
#             has_special = True

#     score = sum([has_digit, has_lower, has_upper, has_special])

#     if len(password) < 8:
#         score = 1

#     if score == 1:
#         return "弱"
#     elif score == 2:
#         return "中"
#     elif score == 3:
#         return "强"
#     elif score == 4:
#         return "极强"

# # 测试示例
# print(password_strength("abc123"))  # 输出：弱
# print(password_strength("Abc123!"))  # 输出：中
# print(password_strength("Abc123!@"))  # 输出：强
# print(password_strength("Abc123!@#"))  # 输出：极强




