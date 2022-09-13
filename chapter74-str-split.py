# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 18:44
s1='hello my lover'
a=s1.split() #括号里表示根据什么去劈分,从字符的左侧开始劈分
print(a) #劈分返回的值是一个列表
b=s1.split(sep=',',maxsplit=1) #最大分劈数量确定为1
print(b)
s2='hello|my|enemy'
c=s2.split(sep='|',maxsplit=1)
print(c)
print()
print(s1.rsplit()) #从右侧开始分割
print(s2.rsplit(sep='|',maxsplit=1))