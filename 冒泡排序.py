# 冒泡排序思想:
# 让一个数字和它相邻的下一个数字进行比较运算
# 如果前一个数字大于后一个数字，交换两个数据的位置

# nums[0]  nums[1]
# nums[1]  nums[2]
# ... ...
# nums[n]  nums[n+1]
# ... ...
# nums[length - 2] nums[length - 1]

# 每一趟比较次数的优化
# 总比较趟数的优化

nums = [5, 1, 7, 6, 8, 2, 4, 3]

for j in range(0, len(nums) - 1):
   for i in range(0, len(nums) - 1 - j):
       if nums[i] > nums[i + 1]:
           a = nums[i]
           nums[i] = nums[i+1]
           nums[i+1] = a

print(nums)
