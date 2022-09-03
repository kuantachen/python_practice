# class 類別(種類)
# 寫 class 的藍圖

class Student:
    def __init__(self, name, score):    # initialize 初始化
        self.name = name
        self.score = score
        print('我誕生了')

    def do_hw(self, hw):
        print('我在做作業', hw)

    def study(self):
        print('我在讀書')
        self.score += 5

    def sleep(self):
        print('我要睡覺了')

s1 = Student('Jacky', 99)    # 創建物件時會先執行初始化的部分    # 存進物件後可以呼叫其他 attribute (屬性 -> 其實是在 class 裡面的 function)
s2 = Student('John', 85)

students = [s1, s2]
for s in students:
    print(s.name, '的分數是', s.score)



# s2.study()
# print(s2.name, s2.score)

# s.do_hw()        
# s.study()
# s.sleep()