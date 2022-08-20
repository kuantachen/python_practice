# dictionary 

words = {
    'ramen': '拉麵',
    'pasta': '義大利麵'
}

# print(words['ramen'])
# print(words['pasta'])

words['tea'] = '茶'

# print(words)

p0 = {
    'name': 'milktea',
    'price': 15
}

p1 = {
    'name': 'greentea',
    'price': 20
}

drinks = [p0, p1]
print(drinks[0]['name'])
print(drinks[1]['price'])