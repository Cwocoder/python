# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
import random

teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
rooms = [[], [], []]
for teacher in teachers:
    room = random.choice(rooms)
    room.append(teacher)
print(rooms)
for i, room in enumerate(rooms):
    print("房间%d里有%d个老师，分别是：" % (i, len(room)))
    for teacher in room:
        print(teacher, end=" ")
    print()
