# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/4 15:54
# 猜哪个碗里有豆子,只有四次机会，用while循环
a=0
while a<4:
    pdd=input('选择你判断的碗号')
    if pdd=='8':
        print('恭喜你选对了，奖金1万')
        break
    else:
        print('选择错误')
        a+=1

# 用for-in循环
for c in range(4):
    d=input('选择你判断的碗号')
    if d=='9':
        print('选择正确')
        break
    else:
        print('选择错误')