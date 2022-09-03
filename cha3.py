def count_products(data):
    chart = {}
    for item in data:
        name, count = item.split(' ')
        count = int(count)
        if name in chart:
            chart[name] += count
        else:
            chart[name] = count
    return chart

data = ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']
print(count_products(data))