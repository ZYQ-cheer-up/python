# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/14 11:07
def fun(a,b=996): #b实在函数的定义处，所以b是形参，而且进行了赋值，所以b称为默认值形参
    print('a=',a)
    print('b=',b)
fun(10,999)
fun(10)
print()
#多个值
def fun1(*args1): #个数可变的位置形参
    print(args1) #元组
def fun2(**args2): #个数可变的关键字形参
    print(args2) #字典
fun1(3,4,564,84,694,464,64)
fun2(a=6464,b=4846394,c=416394)
print()
def fun4(a,b,*,c,d): #从*往后的参数，在函数调用时，只能采用关键字参数传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
#调用
#fun4(11,22,33,44) #位置实参传递 fun4(11,22,33,44) #位置实参传递
#TypeError: fun4() takes 2 positional arguments but 4 were given
print()
fun4(a=10,b=20,c=30,d=40) #关键字实参传递
print()
fun4(13,34,c=99,d=88) #前两个参数是位置实参传参，后两个采用的是关键字实参传参
print()
#函数定义时的形参的顺序问题
def fun5(a,b,*,c,d,**args1):
    pass
def fun6(*args1,**args2):
    pass
def fun7(a,b=10,*args2,**args3):
    pass

