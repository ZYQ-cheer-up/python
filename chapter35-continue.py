# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/4 16:07
# 用for-in输出1-50之间所有5的倍数
a=1 #初始化变量
while a<51: #判断条件
    if not bool(a%5==0): #循环体
        a+=1 #改变变量
        continue
    else:
        print(a)
        a+=1
#用while循环
a=1
for a in range(51):
    if not bool(a%5==0):
        a+=1
        continue
    else:
        print(a)
        a+=1