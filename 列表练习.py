# 有一个列表names，保存了一组姓名names=['zhangsan','lisi','chris','jerry','henry']，
# 再让用户输入一个姓名，如果这个姓名在列表里存在，提示用户姓名已存在；如果这个姓名在列表里不存在，就将这个姓名添加到列表里。
names = ['zhangsan', 'lisi', 'chris', 'jerry', 'henry']
a = input("请输入一个姓名：")
if a in names:
    print('此姓名已存在')
else:
    names.append(a)
    print(names)
