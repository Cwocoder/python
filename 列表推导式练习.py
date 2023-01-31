# 请写出一段 Python 代码实现分组一个 list 里面的元素,比如 [1,2,3,...100]变成 [[1,2,3],[4,5,6]....]
a = [x for x in range(1, 101)]
b = [a[x:x + 3] for x in range(0, len(a), 3)]
print(b)
