from fileinput import filename
from genericpath import isfile
import os    # Operating System

# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue    # 繼續 跳到下一回
            # 先去除掉頭尾的 \n 再 split
            name, price = line.strip().split(',')
            products.append([name, price])
    return products


# 請使用者輸入
# 二維度清單
def user_input(products):
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
    return products


# 印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])


# 寫入檔案
# 有 open 就要有 close, with 是為了方便 python 設計來 "自動 close 的"
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            # 寫入
            f.write(p[0] + ',' + str(p[1]) + '\n')


# main function
def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('檔案存在')
        products = read_file(filename)
    else:
        print('檔案不存在')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()

# function 盡量只做一件事就好 簡潔 單一
# refactor 重構