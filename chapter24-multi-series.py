# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/2 8:34
# 嵌套if
# 商场有无会员打折，消费一定额度打折
answer=input('您是会员吗？y/n') # 判断是否为会员
money=float(input('请您输入消费金额')) # 定义消费金额
if answer=='y': # 是会员
    print('是会员')

    if money>=200:
        print('打九折，付款金额为',money*0.8) # print内同时输出字符串与带运算符的计算表达式print('',表达式)
    elif money>=100:
        print('打八折，付款金额为',money*0.9)
    elif money<100:
        print('不打折，付款金额为',money)
else :
    print('不是会员')
    if money>=200:
        print('打九点五折，付款金额为',money*0.95)
    elif money<200:
        print('不打折，付款金额为',money)