import csv

# csv_path = r'csv-lab.csv'
# with open(csv_path) as f:
#     reader = csv.reader(f)
#     headers = next(reader)
#     print('Headers:', headers)
#     for row in reader:
#         print(row)


# with open(csv_path) as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)
#         print(row['hostname'], row['model'])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Huawei', '5700', 'Beijing'],
#         ['sw2', 'Huawei', '3700', 'Shanghai'],
#         ['sw3', 'Huawei', '9300', 'Guangzhou'],
#         ['sw4', 'Huawei', '9306', 'Shenzhen'],
#         ['sw5', 'Huawei', '12800', 'Hangzhou']]

csv_path = r'F:\hcie-sdn\代码\csv_lab_w.csv'
# with open(csv_path, 'w', newline='') as f:
#     writer = csv.writer(f)
#     for row in data:
#         writer.writerow(row)

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Huawei', '5700', 'Beijing,Xicheng'],
#         ['sw2', 'Huawei', '3700', 'Shanghai'],
#         ['sw3', 'Huawei', '9300', 'Guangzhou,Tianhe'],
#         ['sw4', 'Huawei', '9306', 'Shenzhen'],
#         ['sw5', 'Huawei', '12800', 'Hangzhou']]
#
# with open(csv_path, 'w', newline='') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
# with open(csv_path) as f:
#     print(f.read())

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Huawei', '5700', 'Beijing,Xicheng'],
#         ['sw2', 'Huawei', '3700', 'Shanghai'],
#         ['sw3', 'Huawei', '9300', 'Guangzhou,Tianhe'],
#         ['sw4', 'Huawei', '9306', 'Shenzhen'],
#         ['sw5', 'Huawei', '12800', 'Hangzhou']]
#
# with open(csv_path, 'w', newline='') as f:
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerows(data)
#
# with open(csv_path) as f:
#     print(f.read())

data = [{
    'hostname': 'sw1',
    'location': 'Beijing,Xicheng',
    'model': '5700',
    'vendor': 'Huawei'
}, {
    'hostname': 'sw2',
    'location': 'Shanghai',
    'model': '3700',
    'vendor': 'Huawei'
}, {
    'hostname': 'sw3',
    'location': 'Guangzhou,Tianhe',
    'model': '9300',
    'vendor': 'Huawei'
}, {
    'hostname': 'sw4',
    'location': 'Shenzhen',
    'model': '9306',
    'vendor': 'Huawei'
}, {
    'hostname': 'sw5',
    'location': 'Hangzhou',
    'model': '12800',
    'vendor': 'Huawei'
}]

with open(csv_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for d in data:
        writer.writerow(d)

with open(csv_path) as f:
    print(f.read())
