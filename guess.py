import random
ans = random.randint(1, 100)
#print('答案: ', ans)
i = 0
while ans > 0:
    a = input('請輸入數字(1~100): ')
    a = int(a)
    i += 1 # i = i + 1
    if a > ans:
	    print('猜錯囉!比答案大')
    elif a < ans:
	    print('猜錯囉!比答案小')
    else:
	    print('答對了!')
	    print('這是你猜的第', i,'次')
	    break
    print('這是你猜的第', i,'次')