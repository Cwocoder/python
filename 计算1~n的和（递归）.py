# 计算1~n的和（递归）
def get_sum(n):
    if n == 0:
        return 0
    return get_sum(n - 1) + n


a = eval(input('请输入要求和的数字：'))
print(get_sum(a))
