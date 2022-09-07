# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/6 15:50
# 流程控制语句break,continue在二重循环中的运用
for i in range(5): #代表外层循环要执行五次
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

for i in range(5): #代表外层循环要执行五次
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()