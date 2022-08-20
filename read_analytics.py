import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)    # ProgressBar 是一個物件 (在 Python 裡每個東西都是物件)
with open('reviews.txt', 'r') as f:                 # 物件的第一個字是大寫 (bar 是一個物件 他的型別是 ProgressBar)
    for line in f:                                  # class ProgressBar (寫類別 = 創作資料型別)
        data.append(line)
        count += 1
        bar.update(count)
print('檔案讀取完成，總共有', len(data), '筆資料')

sum_len = 0
for i in data:
    sum_len += len(i)

print('留言平均長度是:', sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('總共有', len(new), '筆留言長度小於100')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到 good')

# List comprehension
# good = [d for d in data if 'good' in d]
# print(good)

# bad = ['bad' in d for d in data]
# print(bad)

# 文字計數
start_time = time.time()

wc = {}
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1    # 新增新的 key 進 wc 字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

end_time = time.time()

print('花了', end_time - start_time, '秒')

while True:
    word = input('請問你要查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('此單字不在字典裡喔！')
print('感謝使用本查詢功能！')
