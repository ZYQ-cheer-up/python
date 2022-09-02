# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/1 15:57
#bool运算符
#and,与
a,b,=10,20,
print(a==10 and b==20) #True and True,还是True
print(a==10 and b<20) #True and False,变成False
print(a!=10 and b==20) #False and True,变成False
print(a!=10 and b!=20) #False and False,还是False

#or,或
print(a==10 or b==20) #True or True,还是True
print(a==10 or b<20) #True or False,还是True
print(a!=10 or b==20) #False or True,还是True
print(a!=10 or b!=20) #False and False,变成False

#not,取反
f1=False
f2=True
print(not f1,not f2)
#一定注意字母大小写

# in and not in
a='my lover'
print('m'in a)
print('e'not in a)
print('m'in a and 'e'not in a)
print('m'in a or 'e'not in a)