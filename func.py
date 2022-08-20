# function 函式/功能

# function 是用來 "收納" 程式碼
# 它是個功能

def wash(dry=False, water=8):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')

    if dry:
        print('烘衣')

wash(True)  # 使用 function
wash()

def say_hi():
    print('Hi~!')
# say_hi()

def add(x=0, y=0):  # 在參數加入預設值
    return x + y

result = add(3, 4)
print(result)

def average(numbers):
    return sum(numbers) / len(numbers)

a = average([1, 2, 3])
print(a)