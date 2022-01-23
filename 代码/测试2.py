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

# list1 = ['关羽', '张飞', '赵云', '马超', '黄忠']
# list2 = ['典韦', '许褚', '张辽', '夏侯惇', '夏侯渊']
#
# for member1 in list1:
#     for member2 in list2:
#         print(f'{member1} 大战 {member2}')

# print ('你好'.encode('utf8')) # 输出 b'\xe4\xbd\xa0\xe5\xa5\xbd'
# print ('你好'.encode('gbk'))  # 输出 b'\xc4\xe3\xba\xc3'

# # 指定编码方式为 utf8
# f = open('tmp.txt', 'w', encoding='utf8')
#
# # write方法会将字符串编码为utf8字节串写入文件
# f.write('白月黑羽：祝大家好运气')
#
# # 文件操作完毕后， 使用close 方法关闭该文件对象
# f.close()


# # 指定编码方式为 gb2312
# f = open('tmp.txt','w',encoding='gb2312')
#
# # write方法会将字符串编码为gb2312字节串存入文件中
# f.write('白月黑羽：祝大家好运气')
#
# # 文件操作完毕后， 使用close 方法关闭该文件对象
# f.close()

# # a 表示 追加模式 打开文件
# f = open('tmp.txt','a',encoding='gb2312')
# f.write('白月黑羽再次祝大家 ：good luck')
# f.close()

# # 指定编码方式为 gbk，gbk编码兼容gb2312
# f = open('tmp.txt','r',encoding='gbk')
#
# # read 方法会在读取文件中的原始字节串后， 根据上面指定的gbk解码为字符串对象返回
# content = f.read()
#
# # 文件操作完毕后， 使用close 方法关闭该文件对象
# f.close()
#
# # 通过字符串的split方法获取其中用户名部分
# name = content.split('：')[0]
#
# print(name)

# f = open('tmp.txt')
# linelist = f.readlines()
# f.close()
# for line in linelist:
#     print(line)

# def fileCopy(srcPath,destPath):
#     srcF = open(srcPath,'rb')
#     content = srcF.read()
#     srcF.close()
#
#     destF = open(destPath,'wb')
#     destF.write(content)
#     destF.close()
#
# fileCopy('1.png','1copy.png')


# with open('tmp.txt') as f:
#     linelist = f.readlines(123)
#     for line in linelist:
#         print(line)


# f = open('0013_a1.txt', 'r', encoding='utf-8')
# list_1 = f.read()
# f.close()
#
#
# ageList = []
# for item in list_1.split('\n'):
#     # 跳过空行
#     if item.strip() == '':
#         continue
#
#     ageList.append(item)
#
# g50 = []  # 大于30岁人员列表
#
# for one_man in ageList:
#     name, age = one_man.split(':')
#     age = int(age.strip())
#     name = name.strip()
#     if age >= 50:
#         g50.append(name)
#
#
# names = ','.join(g50)
# print(names)

# import stock.food.beef
#
# stock.food.beef.stockleft()

# import requests
# def getStockPrice(stockName):
#
#     # 构造 HTTP 请求
#     url = f'http://hq.sinajs.cn/list={stockName}'
#
#     # 返回的response 对应响应消息的对象
#     response = requests.get(url)
#
#     # 返回的内容在消息体中，通过text属性获取
#     info = response.text
#     print(info)
#
#     # 返回的是这种格式 大秦铁路, 27.55, 27.25, 26.91,
#     # 通过split 方法截取
#     price = info.split(',')[1]
#
#     return price
#
#
# price = getStockPrice('sh601006')
# print(price)

# members = {
#     'account1': 13,
#     'account2': 12
# }
#
# val = members.pop('account1')
# print(members)
# print(val)

# members = {
#     'account1': 13,
#     'account2': 12
# }
#
# if 'account1' in members:
#     print('account1 在字典中存在')
#
# if 'account88' not in members:
#     print('account88 不在字典中')

# members = {
#     'account1': 13,
#     'account2': 12,
#     'account3': 15,
# }
#
# for account, level in members.items():
#     print(f'account:{account}, level:{level}')

# with open('0016_1.txt',encoding='utf-8') as f:
#     in_form_list = f.read().splitlines()
#
# print(in_form_list)
#
# coin_table = {}
#
# for info in in_form_list:
#
#     # 先去除左右空白字符
#     info = info.strip()
#
#     # 如果是空行，跳过
#     if not info:
#         continue
#
#     parts = info.split(' ')
#     name = parts[0]
#     coin = int(parts[-2])
#
#     # 如果姓氏还没有在统计表中
#     # 创建新元素
#     if name[0] not in coin_table:
#         coin_table[name[0]] = coin
#
#     # 如果姓氏已经在统计表中
#     # 累加积分
#     else:
#         coin_table[name[0]] += coin
#
# for name1,coins in coin_table.items():
#     print(f'{name1} : {coins}')

# from pprint import pprint
#
# members = {
#     1: {'name': '白月黑羽', 'level': 3, 'coins': 300},
#     2: {'name': '短笛魔王', 'level': 5, 'coins': 330},
#     3: {'name': '紫气一元', 'level': 6, 'coins': 340},
#     4: {'name': '拜月主', 'level': 3, 'coins': 32200},
#     5: {'name': '诸法空', 'level': 4, 'coins': 330},
#     6: {'name': '暗光城主', 'level': 3, 'coins': 320},
#     7: {'name': '心魔尊', 'level': 3, 'coins': 2300},
#     8: {'name': '日月童子', 'level': 8, 'coins': 3450},
#     9: {'name': '不死尸王', 'level': 3, 'coins': 324},
#     10: {'name': '天池剑尊', 'level': 9, 'coins': 13100},
# }
#
# # 因为要根据用户名查找用户信息，需要改变字典格式
# # 以用户名为key，创建一个字典
#
# name2info = {}
# for k, v in members.items():
#     name = v['name']
#     # 因为id也是要查询的内容，加到 字典的 value值中
#     v['id'] = k
#     name2info[name] = v
#
#
# # 定义查看用户账号的处理函数
# def check_account():
#     name = input('请输入查找的用户账号:')
#     if name not in name2info:
#         print(f'对不起，账号 {name} 不存在.')
#         return
#
#     info = name2info[name]
#     print(f'账号: {name} , ID : {info["id"]} , 等级：{info["level"]} , 金币：{info["coins"]} ')
#
#
# # 定义添加用户账号的处理函数
# def add_account():
#     while True:
#         name = input('请输入添加用户的账号:')
#         if name in name2info:
#             print('对不起，该账号已经存在')
#         else:
#             break
#
#     while True:
#         level = input('请输入该用户的等级:')
#         # 如果不是数字 ， 则输入格式错误
#         if not level.isdigit():
#             print('对不起，等级必须为一个数字')
#         else:
#             level = int(level)  # 转化为整数
#             break
#
#     while True:
#         coins = input('请输入该用户的金币数量:')
#         # 如果不是数字 ， 则输入格式错误
#         if not coins.isdigit():
#             print('对不起，金币数 必须为一个数字')
#         else:
#             coins = int(coins)  # 转化为整数
#             break
#
#     # 要产生一个不存在的ID号， 这里我们取 当前最大的ID号+ 1
#     new_id = max(members.keys()) + 1
#     # 注意： 两个字典里面都要添加
#     members[new_id] = {'name': name, 'level': level, 'coins': coins}
#     name2info[name] = {'name': name, 'level': level, 'coins': coins, 'id': new_id}
#
#
# # 定义删除用户账号的处理函数
# def del_account():
#     name = input('请输入要删除的用户账号:')
#     if name not in name2info:
#         print(f'对不起，账号 {name} 不存在.')
#         return
#
#     # 注意： 两个字典里面都要删除
#     the_id = name2info[name]['id']
#     name2info.pop(name)
#     members.pop(the_id)
#
#
# # 定义打印表内容的处理函数
# def show_tables():
#     print('\n现在name2info的表内容是：\n')
#     pprint(name2info)
#     print('\n现在members的表内容是：\n')
#     pprint(members)
#
#
# menu = '''
# 请选择操作选项：
#    1 查看用户账号信息
#    2 添加用户
#    3 删除用户
#    4 列出所有用户信息
#    0 退出
# '''
# # 显示主菜单
# while True:
#     choice = input(menu)
#
#     # 选择查看查看用户账号
#     if choice == '1':
#         check_account()
#     elif choice == '2':
#         add_account()
#     elif choice == '3':
#         del_account()
#     elif choice == '4':
#         show_tables()
#     elif choice == '0':
#         break

# class BenzCar:
#     brand = '奔驰'
#     country = '德国'
#
#     @staticmethod
#     def pressHorn():
#         print('嘟嘟~~~~~~')
#
#
# BenzCar.pressHorn()

# class BenzCar:
#     brand = '奔驰'
#     country = '德国'
#
#     @staticmethod
#     def pressHorn():
#         print('嘟嘟~~~~~~')
#
#
# car1 = BenzCar()
# print(car1.brand)
# car1.pressHorn()

# 轮胎
# class Tire:
#     def __init__(self, size, createDate):
#         self.size = size  # 尺寸
#         self.createDate = createDate  # 出厂日期
#
#
# class BenzCar:
#     brand = '奔驰'
#     country = '德国'
#
#     def __init__(self, color, engineSN, tires):
#         self.color = color  # 颜色
#         self.engineSN = engineSN  # 发动机编号
#         self.tires = tires
#
#
# # 创建4个轮胎实例对象
# tires = [Tire(20, '20160808') for i in range(4)]
# car = BenzCar('red', '234342342342566', tires)
#
# print(car.tires[0].size)

# def equals(*nums):
#     # 定义统计表
#     stats = {}
#     for num in nums:
#         # 已经在统计表中
#         if num in stats:
#             stats[num] += 1
#         # 不在统计表中
#         else:
#             stats[num] = 1
#
#     for num, times in stats.items():
#         print(f'数字 {num} 出现了 {times} 次')
#
#
# equals(3, 4, 3, 4, 1, 6, 2)

# import os
# os.makedirs('tmp/pyrhon3/fileop',exist_ok=True)

from subprocess import PIPE, Popen

# 返回的是 Popen 实例对象
proc = Popen(
    'fsutil volume diskfree c:',
    stdin=None,
    stdout=PIPE,
    stderr=PIPE,
    shell=True)

# communicate 方法返回 输出到 标准输出 和 标准错误 的字节串内容
# 标准输出设备和 标准错误设备 当前都是本终端设备
outinfo, errinfo = proc.communicate()

# 注意返回的内容是bytes 不是 str ，我的是中文windows，所以用gbk解码
outinfo = outinfo.decode('gbk')
errinfo = errinfo.decode('gbk')
print(outinfo)
print('-------------')
print(errinfo)

outputList = outinfo.splitlines()

# 剩余量
free = int(outputList[0].split(':')[1].replace(',', '').split('(')[0].strip())

# 总空间
total = int(outputList[1].split(':')[1].replace(',', '').split('(')[0].strip())

if (free / total < 0.1):
    print('!! 剩余空间告急！！')
else:
    print('剩余空间足够')
