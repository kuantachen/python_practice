password = 'a123456'
i = 3
while i > 0:
    i = i - 1
    pwd = input("請輸入密碼: ")
    if pwd == password:
        print("登入成功！")
        break
    else:
        print("密碼錯誤！")
        if i > 0:
            print("還有 ", i, " 次機會！")
        else:
            print("密碼錯誤太多次，請稍後再輸入")

