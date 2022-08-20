# class 類別(種類)
# 寫 class 的藍圖

class Student:
    def __init__(self):    # initialize 初始化
        print('我誕生了')

    def do_hw(self):
        print('我在做作業')

    def study(self):
        print('我在讀書')

    def sleep(self):
        print('我要睡覺了')

s = Student()    # 創建物件時會先執行初始化的部分
s.do_hw()        # 存進物件後可以呼叫其他 attribute (屬性 -> 其實是在 class 裡面的 function)
s.study()
s.sleep()