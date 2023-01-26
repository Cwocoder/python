# 判断用户输入的字符是否在字符串里
word = "hello"
x = input("请输入一个字符")
for c in word:
    if c == x:
        print("该字符存在")
        break
else:
    print("该字符不存在")
