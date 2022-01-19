def in_weather():
    # 输入气温和气压
    temperature = input('请输入今天气温（单位 摄氏度）:')
    air_pressure = input('请输入今天气压（单位 帕）:')
    return temperature, air_pressure


def weather(temperature, air_pressure):
    # 进行判断
    if 25 < temperature <= 30 and 200 < air_pressure <= 300:
        print('比较舒适')
    elif 10 < temperature <= 25 and 100 < air_pressure <= 200:
        print('特别舒适')
    elif -8 <= temperature <= 10 and 20 <= air_pressure <= 100:
        print('比较舒适')
    elif 30 < temperature or temperature < -8:
        print('不舒适')
    elif 300 < air_pressure or air_pressure < 20:
        print('不舒适')
    else:
        print('本程序不能判断')
    return


data = in_weather()
weather(int(data[0]), int(data[1]))
