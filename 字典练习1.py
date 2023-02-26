# 1.有一个列表persons，保存的数据都是字典
# persons = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 20},
# {'name': 'wangwu', 'age': 19},{'name': 'jerry', 'age': 21}]
# 要求让用户输入一个姓名，如果这个姓名在列表里存在，就提示用户名称已存在，添加失败，
# 如果这个姓名在列表里不存在，提示让用户输入年龄，并将用户输入的姓名和年龄添加到这个列表里。
persons = [{'name': 'zhangsan', 'age': 18}, {'name': 'lisi', 'age': 20}, {'name': 'wangwu', 'age': 19},
           {'name': 'jerry', 'age': 21}]
name = input('请输入一个姓名:')
for person in persons:
    if person['name'] == name:
        print('用户名称已存在，添加失败')
        break
else:
    age = input('请输入年龄：')
    persons.append({'name': name, 'age': age})
print(persons)
