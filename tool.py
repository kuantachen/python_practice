from db import Db    # from 檔案 import class


class Tool:
    def __init__(self):
        print('test')
        self.db = Db()

    def trytest(self):
        self.db.insert_data()    # class 跟 class 間交互使用 (通常會分開檔案放)