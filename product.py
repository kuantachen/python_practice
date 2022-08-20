from genericpath import isfile
import os    # Operating System

products = []
if os.path.isfile('products.csv'):
    print('檔案存在')
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue    # 繼續 跳到下一回
            # 先去除掉頭尾的 \n 再 split
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('檔案不存在')


# 請使用者輸入
# 二維度清單
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    # p = []
    # p.append(name)
    # p.append(price)
    # p = [name, price]
    # products.append(p)
    products.append([name, price])

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
# 有 open 就要有 close, with 是為了方便 python 設計來 "自動 close 的"
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        # 寫入
        f.write(p[0] + ',' + str(p[1]) + '\n')