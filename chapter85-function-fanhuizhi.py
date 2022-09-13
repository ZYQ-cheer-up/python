# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/13 10:55
def fun(num):
    odd=[] #存奇数
    even=[] #存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
a=fun([1,52,8,4,6,7,6,4,8,4163,4,68,65,21,842,86])
print(a) #函数返回多个值时，结果为元组
'''函数的返回值
（1）若果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】，return可以不写
（2）函数的返回值，若果是一个，则直接返回类型
（3）函数的返回值，若果有多个，返回的结果为元组'''
print()
def fun1():
    print('hello')
    #return
fun1()
print()
def fun2():
    return'hello'
res=fun2()
print(res)
print()
def fun3():
    return'hello','Python'
print(fun3())