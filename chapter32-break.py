# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/4 15:20
# 银行卡密码最多输入三次，三次内输入正确就break
for secret in range(3): # 表示遍历三次
    pwd =input('请输入您的银行卡密码：') #初始化变量
    if pwd=='686866': # 判断条件
        print('密码正确')
        break
    else:
        print('密码错误')

# 用while循环
a=0 # 初始化变量
while a<3: # 条件判断
    pwd = input('请输入您的银行卡密码') # 循环体
    if pwd=='686688':
        print('密码正确')
        break
    else:
        a+=1 # 改变变量
        print('密码错误')