import random
ans = random.randint(1, 100)
print('答案: ', ans)
while ans > 0:
    a = input('請輸入數字(1~100): ')
    a = int(a)
    if a > ans:
	    print('猜錯囉!比答案大')
    elif a < ans:
	    print('猜錯囉!比答案小')
    else:
	    print('答對了!')
	    break