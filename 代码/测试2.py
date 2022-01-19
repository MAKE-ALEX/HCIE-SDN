# str1 = '大家好，我的名字叫：'
# str2 = '黑羽白月'
#
# print(str1 + str2)


# name = input('输入你的名字:')
# age = input('输入你的年龄:')
#
# print(f'你的名字是：{name}， 你的年龄是{age}')

# info = [
#     ['user1', 345.6, 12, '黄金'],
#     ['user2', 2345.6, 8, '白银'],
#     ['user3555', 55345.6, 22, '钻石'],
# ]
#
# print(f'用户：{info[0][0]:>8}， 积分：{info[0][1]:>8}， 等级：{info[0][2]:>3}， 头衔：{info[0][3]:<5}')
# print(f'用户：{info[1][0]:>8}， 积分：{info[1][1]:>8}， 等级：{info[1][2]:>3}， 头衔：{info[1][3]:<5}')
# print(f'用户：{info[2][0]:>8}， 积分：{info[2][1]:>8}， 等级：{info[2][2]:>3}， 头衔：{info[2][3]:<5}')

# command = input("请输入命令:")
# while command != 'exit':
#     print(f'输入的命令是{command}')
#     command = input("请输入命令")

# i = 1
# while i <= 1000:
#     print(i)
#     i += 1

# studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']
#
# for student in studentAges:
#     print(student)

# for n in range(100):
#     print(n)
#     print('python，我爱你')

# for n in range(50,101):
#     print(n)

# for n in range(50,101,5):
#     print(n)

# studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']
#
# # enumerate (studentAges) 每次迭代返回 一个元组
# # 里面有两个元素，依次是 元素的索引和元素本身
# for idx, student in enumerate(studentAges):
#     if int(student.split(':')[-1]) >= 17:
#         print(idx)

# while True:
#     command = input("请输入命令:")
#     if command == 'exit':
#         break
#     print(f'输入的命令是{command}')
#
# print('程序结束')

# for i in range(100):
#     command = input("请输入命令:")
#     if command == 'exit':
#         break
#     print(f'输入的命令是{command}')
#
# print('程序结束')

# while True:
#     command = input("请输入命令:")
#     if command == 'exit':
#         break
#     if command == 'cont':
#         continue
#     print(f'输入的命令是{command}')
#
# print('程序结束')

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = []
# for num in list1:
#     list2.append(num * num)
#
# print(list2)

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [num **3 for num in list1]
# print(list2)

list1 = ['关羽', '张飞', '赵云', '马超', '黄忠']
list2 = ['典韦', '许褚', '张辽', '夏侯惇', '夏侯渊']

for member1 in list1:
    for member2 in list2:
        print(f'{member1} 大战 {member2}')
