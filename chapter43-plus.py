# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/6 10:54
for i in range(1,10): #确定行数
    for j in range(1,i+1): #判断行与列的关系
        print(i,'*',j,'=',i*j,end='\t') #打印乘法口诀表
    print()
a=1 #初始化变量
while a<10: #条件判断
    for i in range(1,a+1): # 循环体，以确定的行列关系
        print(i,'*',a,'=',i*a,end='\t')
    print()
    a+=1 #改变变量