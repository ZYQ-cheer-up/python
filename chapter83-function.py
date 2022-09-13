# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/13 9:31
#函数的创建
def calc(a,b): #a,b为形式参数，成为形参，形参的位置在函数的定义处
    c=a*b
    return c
print()
#函数的调用
result=calc(10,20) #10，20为实际参数，称为实参，实参的位置在函数的调用处
print(result) #位置实参
print()
r=calc(b=9,a=10) #关键字实参
print(r)
