# 1.有一个字典dict1 ={"a":100,"b".200,"c"}，使用代码，将字典的key和value互换，变成{100:"a",200:"b",300:"c”}
dict1 = {"a": 100, "b": 200, "c": 300}
dict2 = {v: k for k, v in dict1.items()}
print(dict2)
