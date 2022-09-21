# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/14 15:44
def fun(a,b):
    c=a+b #c称为局部变量，因为c是在函数体内部进行定义的变量，a,b为函数的形参没作用范围也是函数的内部，相当于局部变量
    print(c)
#print(a)NameError: name 'a' is not defined #超出了作用范围（不在作用域内）

name='zhong' #name的作用范围为函数内部外部都可以使用，称为全局变量
print(name)
def fun1():
    print(name)
fun1()
print()
def fun2():
    global age #函数内部定义的局部变量，使用global声明之后就变成了全局变量：global+局部变量
    age=26
    print(age)
fun2()
#print(age) NameError: name 'age' is not defined
print(age) #必须要加上一个global age