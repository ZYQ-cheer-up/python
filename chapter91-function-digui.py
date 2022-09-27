# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/14 15:58
#用递归函数来计算阶乘
def fac(n):
    if n==1:
        return 1
    else:
        res=n*fac(n-1)
        return res
print(fac(7))