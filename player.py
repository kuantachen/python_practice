from unicodedata import name


class Player():
    def __init__(self, name, atk):    # 屬性最好都寫在 __init__ 裡面
        print('玩家登入成功！')
        self.name = name
        self.hp = 100
        self.atk = atk

    def attack(self, target):
        print(self.name, 'attacking', target.name)
        target.hp = target.hp - self.atk


p1 = Player('Player1', 5)    # 實體化 (instantiation)
p2 = Player('Player2', 10)
p1.attack(p2)
print(p2.hp)

# class 裡面的 function 會叫 method (其實作用一樣)
# 若不是在 class 裡面，兩個 function 間空2行，method 空一行