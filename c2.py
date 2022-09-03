from turtle import color


class Desk:
    def __init__(self, color):
        self.color = color
        print('我被製造出來了')

    def re_color(self, new_color):
        self.color = new_color
d = Desk('Blue')    # instantiation 實體化 (創造出物件)
d.re_color('Red')
print(d.color)