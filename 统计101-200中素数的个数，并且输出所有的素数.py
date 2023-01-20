# 统计101-200中素数的个数，并且输出所有的素数。 (索数又叫质数，就是只能被1和它本身整除的数)
a = 0
for i in range(101,201):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)
        a += 1
print("101-200中素数的个数为：",a)
