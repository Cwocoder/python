# 请删除列表 words = ['hello','',',','good','hi','','yes','','no'] 里所有的空字符串。
words = ['hello', '', ',', 'good', 'hi', '', 'yes', '', 'no']
while '' in words:
    words.remove('')
    if '' not in words:
        break
print(words)
