
data = []

# 自動 close file
with open('food.txt', 'r') as f:
    for line in f:
        data.append(line.strip())  # 去除掉換行符號

print(data)