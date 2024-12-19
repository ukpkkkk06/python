for x in range(0, 21):  
    for y in range(0, 34):  
        z = 100 - x - y 
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f"公鸡{x}只，母鸡{y}只，小鸡{z}只")
import random
mapping = {0: "石头", 1: "剪刀", 2: "布"}
player_choice = int(input("请输入你的出拳（0代表石头，1代表剪刀，2代表布）："))
computer_choice = random.randint(0, 2)
print(f"你出的是{mapping[player_choice]}，电脑出的是{mapping[computer_choice]}")
if player_choice == computer_choice:
    result = "平局"
elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (
        player_choice == 2 and computer_choice == 0):
    result = "你赢了"
else:
    result = "电脑赢了"
print(result)
print("以下是所有可能的情况及结果：")
for i in range(3):
    for j in range(3):
        print(f"你出{mapping[i]}，电脑出{mapping[j]}，结果：", end="")
        if i == j:
            print("平局")
        elif (i == 0 and j == 1) or (i == 1 and j == 2) or (i == 2 and j == 0):
            print("你赢了")
        else:
            print("电脑赢了")
red_scores = [0, 0, 0]
blue_scores = [0, 0, 0]
def record_score(team, score_type, score):
    """
    记录得分的函数
    :param team: 队伍名称，取值为'red'（红队） 或者 'blue'（蓝队）
    :param score_type: 得分类型，取值为'1'（罚球得分）、'2'（两分球得分）、'3'（三分球得分）
    :param score: 此次得分的分值
    """
    if team == 'red':
        if score_type == '1':
            red_scores[0] += score
        elif score_type == '2':
            red_scores[1] += score
        elif score_type == '3':
            red_scores[2] += score
    elif team == 'blue':
        if score_type == '1':
            blue_scores[0] += score
        elif score_type == '2':
            blue_scores[1] += score
        elif score_type == '3':
            blue_scores[2] += score
def get_total_score(team):
    """
    获取队伍总分的函数
    :param team: 队伍名称，取值为'red'（红队） 或者 'blue'（蓝队）
    :return: 对应队伍的总分
    """
    if team == 'red':
        return sum(red_scores)
    elif team == 'blue':
        return sum(blue_scores)
def get_three_point_score(team):
    """
    获取队伍三分球得分的函数
    :param team: 队伍名称，取值为'red'（红队） 或者 'blue'（蓝队）
    :return: 对应队伍的三分球总得分
    """
    if team == 'red':
        return red_scores[2]
    elif team == 'blue':
        return blue_scores[2]
while True:
    print("请选择操作：")
    print("1. 记录得分")
    print("2. 查询队伍总分")
    print("3. 查询队伍三分球得分")
    print("4. 退出程序")
    choice = input()
    if choice == '1':
        team = input("请输入队伍（red表示红队，blue表示蓝队）：")
        score_type = input("请输入得分类型（1表示罚球得分，2表示两分球得分，3表示三分球得分）：")
        score = int(input("请输入得分分值："))
        record_score(team, score_type, score)
    elif choice == '2':
        team = input("请输入要查询总分的队伍（red表示红队，blue表示蓝队）：")
        total_score = get_total_score(team)
        print(f"{team}队的总分为：{total_score}")
    elif choice == '3':
        team = input("请输入要查询三分球得分的队伍（red表示红队，blue表示蓝队）：")
        three_point_score = get_three_point_score(team)
        print(f"{team}队的三分球总得分：{three_point_score}")
    elif choice == '4':
        break
    else:
        print("输入的操作选项无效，请重新输入！")
family_population = int(input("请输入家庭人口数："))
wage_income = int(input("请输入工资性收入："))
business_income = int(input("请输入家庭经营性收入："))
transfer_income = int(input("请输入转移性收入："))
property_income = int(input("请输入财产性收入："))
operational_expense = int(input("请输入生产经营性支出："))
per_capita_income = (wage_income + business_income + transfer_income + property_income - operational_expense) / family_population
poverty_standard = 4000
if per_capita_income < poverty_standard:
    print("认定为贫困户")
else:
    dropout_question = input("是否有子女在义务教育阶段因贫辍学？（是/否）")
    illness_question = input("是否有家庭成员患大病或长期慢性病，刚性支出较大，直接影响了正常生产生活？（是/否）")
    housing_question = input("是否无房或居住用房是C、D级危房，且无其他安全住房？（是/否）")
    if dropout_question == "是" or illness_question == "是" or housing_question == "是":
        print("认定为贫困户")
    else:
        print("不予认定贫困户")
import random
def fhb(money, n):
    list_result = []
    remain_money = money
    for i in range(n - 1):
        min_value = 1
        max_value = remain_money - (n - i - 1)
        one_money = random.randint(min_value, max_value)
        list_result.append(one_money)
        remain_money -= one_money
    list_result.append(remain_money)
    return list_result
money = int(input("请输入红包总金额："))
n = int(input("请输入红包数量："))
way = input("请选择分红包方式（输入'r'表示随机分红包）：")
if way == "r":
    result_list = fhb(money, n)
    for index, r in enumerate(result_list):
        print("第{}个红包金额为：{}元".format(index + 1, str(r)))
