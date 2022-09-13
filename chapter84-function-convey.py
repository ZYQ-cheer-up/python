# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/13 10:09
def calc(a,b,c):
    d=a*b-c
    return d
e=calc(9,10,3)
print(e)
print()
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1',arg1)
    print('arg2',arg2)
    #return
print()
n1=10 #字符串，属于不可变对象
n2=[20,30,40,50] #列表属于可变对象
print('n1',n1)
print('n2',n2)
fun(n1,n2) #位置传参，arg1,arg2是函数定义处的形参，n1,n2,时函数调用处的实参，形参与实参可以不同名
print('n1',n1)
print('n2',n2)
#在函数的调用过程中，如果参数传递的是不可变对象，在函数体当中的修改不会影响实参的值 arg1的修改不会影响n1
#如果是可变对象，在函数体当中的修改就会影响到实参的值 arg2的修改会影响到n2