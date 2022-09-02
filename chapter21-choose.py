# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/1 20:13
money=10000 # 余额
a=int(input('请输入取款金额')) #取款金额
# 判断余额是否充足
if money>=a:
    money=money-a
    print('取款成功，余额为',money)

store=20
b=int(input('请挑选盲盒数量')) #购买数量
if store>=b:
    store=store-b
    print('商品购买成功，剩余盲盒',store)