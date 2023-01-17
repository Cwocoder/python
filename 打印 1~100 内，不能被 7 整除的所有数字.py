# 1、打印 1~100 内，不能被 7 整除的所有数字。
i=0
while i<100:
    i+=1
    if i%7==0:
        continue
    else:
        print(i)
