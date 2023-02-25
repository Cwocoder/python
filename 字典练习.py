# 字典练习：列表里元素的数据统计用字典输出
chars = ['a', 'c', 'x', 'd', 'p', 'a', 'p', 'a', 'c']
char_count = {}
for char in chars:
# if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

    if char not in char_count:
        char_count[char] = chars.count(char)
print(char_count)
