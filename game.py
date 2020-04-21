import random

answer = random.randint(1,10)
count = 6

while count > 0:
    
    temp = input("猜一下我心里想的是哪个数字：")
    
    while not temp.isdigit():
        print("抱歉，输入不合法")
        temp = input('请输入一个整数：')
        
    num = int(temp)
    
        
    if num == answer:
        print("你真聪明，" + '不过没有奖励哦\(^o^)/~')
        break
    
    else:
        
        if num > answer:
            print('大啦！！')
        else:
            print('小啦！！')
            
    count = count - 1
    
    if count == 1:
        print('笨蛋，还有一次机会哦^_^')
    else:
        if 1 < count <= count: 
            print('加油，小伙！')
        
print('游戏结束，不玩啦')
