# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/6 9:05
#银行卡密码输入系统，三次错误锁定
for pdd in range(3):
    pdd=input('请输入您的密码')
    if pdd=='999999':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('sorry,you have mistake entering correct number for three times,please ask our worker for help')
a=0
while a<3:
    pdd=input('please enter your number')
    if pdd=='686866':
        print('correct')
        break
    else:
        a+=1
        print('false')
else:
    print('sorry,you have mistake entering correct number for three times,please ask our worker for help')