
# Lesson 47:猜數字遊戲
# 產生一個隨機整數1-100(不要印出來)
# 讓user重覆輸入數字去猜
# 猜對的話 印出 "終於猜對惹"
# 猜錯的話 要告訴他 比答案大/小

import random
r = random.randint(1,100) 
print(r)

while True:
    num = input('請輸入數字玩猜猜樂歐~')
    num = int(num)
    if num == r:
        print('終於猜對惹')
        break
            # break
            # 在單獨只有if的statement裡面不能用break中斷程式
            # 运行时报错：SyntaxError: 'break' outside loop。
            # 原来break只能在for和while迴圈中使用。
            # https://stackoverflow.com/questions/2462566/python-break-outside-loop
            # Because "break" can only be used inside a loop. 
            # It is used to break out of a loop (stop the loop).
    elif num > r:
        print('再猜小一點')
    else:
        print('再猜大一點')
