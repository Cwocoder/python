# 2、计算 1~100 内，所有不能被 7 整除的数字之和。
i = 0
sum = 0
while i < 100:
    i += 1
    if i % 7 == 0:
        continue
    else:
        sum += i
print(sum)
