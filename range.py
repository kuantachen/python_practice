# range 範圍
# python 內建功能: 清單產生器
# 通常只是為了拿來重複執行固定次數

import random

for i in range(3):
    r = random.randint(1, 1000)
    print('這是第', i + 1, '次產生隨機數:', r)

# range(2, 10, 3) # [2, 5, 8]
# range(start, end, step)