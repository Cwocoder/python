# 从键盘输入身高，如果身高没有超过150cm，则进动物园不用买票，否则需要买票。
height=int(input("请输入你的身高："))
if height<=150:
    print("无需买票")
else:
    print("需要购票")
