# def in_weather():
#     # 输入气温和气压
#     temperature = input('请输入今天气温（单位 摄氏度）:')
#     air_pressure = input('请输入今天气压（单位 帕）:')
#     return temperature, air_pressure
#
#
# def weather(temperature, air_pressure):
#     # 进行判断
#     if 25 < temperature <= 30 and 200 < air_pressure <= 300:
#         print('比较舒适')
#     elif 10 < temperature <= 25 and 100 < air_pressure <= 200:
#         print('特别舒适')
#     elif -8 <= temperature <= 10 and 20 <= air_pressure <= 100:
#         print('比较舒适')
#     elif 30 < temperature or temperature < -8:
#         print('不舒适')
#     elif 300 < air_pressure or air_pressure < 20:
#         print('不舒适')
#     else:
#         print('本程序不能判断')
#     return
#
#
# data = in_weather()
# weather(int(data[0]), int(data[1]))


# str1 = '''
# 熊宁
# 杰益
#
# 王伟伟
#
# 青芳
#
# 玉琴
# 焦候涛
# 莫福
# 杨高旺
# 唐欢欢
# 韩旭
# '''
#
# str2 = '''
# 焦候涛
# 熊宁
# 玉琴
#
# 骆龙
#
# 韩旭
# 杨高旺
#
#
# 杰益
#
# 莫福
#
# 伟伟
#
# 李福
# '''
#
#
# def git_name_list(name_str):
#     names = []
#     line_list = name_str.splitlines()
#     for line in line_list:
#         name_lin = line.strip()
#         if name_lin != '':
#             # 不等于空
#             names.append(name_lin)
#             continue
#     return names
#
#
# names_1 = git_name_list(str1)
# names_2 = git_name_list(str2)
#
# print(names_1)
# print(names_2)
#
# for name in names_1:
#     if name not in names_2:
#         print(name)
#
# print()
#
# for name in names_2:
#     if name not in names_1:
#         print(name)

ageTable = '''
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'''

# def git_name_age(data_1):
#     line_ll = []
#     line_list = data_1.splitlines()
#     # 以换行分割
#     for line in line_list:
#         line_list = line.strip()
#         # 去左右空格
#         if line_list != '':
#             # 不等于空
#             line_ll.append(line_list)
#             continue
#     return line_ll
#
#
# def split_name_age(data_2):
#     wj_name = []
#     for n in data_2:
#         wj_name.append(n.split(', ')[0])
#         continue
#     return wj_name
#
#
# def split_age(data_3):
#     wj_age = []
#     for n in data_3:
#         wj_age.append(n.split(', ')[1])
#         continue
#     return wj_age
#
#
# list_wj_age = git_name_age(ageTable)
# print(list_wj_age)
#
# age_list = split_age(list_wj_age)
# print(age_list)
#
# name_list = split_name_age(list_wj_age)
# print(name_list)
#
# if age_list >= 30:
#     g30.append(name)


# ageList = []
# for line in ageTable.splitlines():
#     nameage = line.replace(' ', '')
#     if nameage != '':
#         ageList.append(nameage)
#
# g30 = []
# l30 = []
# name = []
# age_1 = []
#
# for nameage in ageList:
#     name, age = nameage.split(',')
#     age_1 = int(age)
#
#     if age_1 >= 30:
#         g30.append(name)
#     else:
#         l30.append(name)
#
# print(g30)
#
# print()
#
# print(l30)

# ageTable = '''
#     诸葛亮, 28
#     刘备, 48
#     刘琦, 25
#     赵云, 32
#     张飞, 43
#     关羽, 45
# '''
#
#
#
# # 先转换成如下格式的列表
# # ageList = [
# #     '诸葛亮, 28',
# #     '刘备, 48',
# #     '赵云, 42',
# #     ....
# # ]
#
# ageList = []
# for item  in ageTable.split('\n'):
#     # 跳过空行
#     if item.strip()  == '':
#         continue
#
#     ageList.append(item)
#
# g30 = []  # 大于30岁人员列表
# l30 = []  # 小于30岁人员列表
# for oneman  in ageList:
#     name,age   = oneman.split(',')
#     age = int(age.strip())
#     name = name.strip()
#     if age >= 30:
#         g30.append(name)
#     else:
#         l30.append(name)
#
#
# print('大于等于30岁的人有：')
# for man in g30:
#     print(man)
#
#
# print('\n小于30岁的人有：')
# for man in l30:
#     print(man)

# def calculate_score(rounds):
#     guan_win_round = 0
#     zhang_win_round = 0
#     ping_round   = 0
#
#     # 取出列表里面每一局round，进行如下处理：
#     for round in rounds:
#         guan = round[0]
#         zhang = round[1]
#
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
#
#         if win == 'g':
#             print('关羽赢')
#             guan_win_round += 1
#         elif win == 'z':
#             print('张飞赢')
#             zhang_win_round += 1
#         elif win == '=':
#             print('平局')
#             ping_round  += 1
#
#     print('\n=============\n')
#     print(f'关羽赢{guan_win_round}次')
#     print(f'张飞赢{zhang_win_round}次')
#     print(f'平局{ping_round}次')
#
#     if guan_win_round> zhang_win_round:
#         print('关羽赢')
#     elif  guan_win_round < zhang_win_round:
#         print('张飞赢')
#     else:
#         print('平局')
#
# calculate_score([['剪刀', '石头'], ['布', '剪刀'], ['剪刀', '剪刀']])
