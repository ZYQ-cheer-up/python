# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/14 9:40
#函数的参数总结
def fun(a,b,c): #a,b,c在函数的定义处，所以都是形式参数
    print('a=',a)
    print('b=',b)
    print('c=',c)

#函数的调用
fun(12,0.23,34) #函数调用时的的参数传递，称为位置传参
print()
lst1=[985,211,3.14]
#fun(lst1) TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(*lst1) #在函数调用时，将列表中的每个元素都转换为位置实参传入
print()
fun(a=996,c=731,b=31.12)
print()
dict={'a':999,'b':993,'c':941}
#fun(dict) TypeError: fun() missing 2 required positional arguments: 'b' and 'c'
fun(**dict) #在函数调用时，将字典中的键值对都转换为关键字实参输入