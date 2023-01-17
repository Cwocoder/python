# 打印九九乘法表
i=0
while i<9:
    i+=1
    j=0
    while j<i:
        j+=1
        print(j,'*',i,'=',(j*i),sep="",end='\t')
    print()
