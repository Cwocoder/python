# 2.求斐波那契数列中第n个数的值，n是正整数
a = int(input("请输入需要的斐波那契数列的序号："))
num1 = 1
num2 = 1
for a in range(0,a-2):
    a = num1
    num1 = num2
    num2 = a + num1
print(num2)
