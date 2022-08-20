import random

start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
    count += 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜中了！')
        break
    elif num > r:
        print('太大了，往下猜')
    elif num < r:
        print('太小了，往上猜')
    print("你猜了", count, "次")