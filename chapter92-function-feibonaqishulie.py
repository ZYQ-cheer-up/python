# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/14 16:20
# 输出第六位的数字
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))
print()
#输出前六位的数字
for i in range(1,7):
    print(fib(i))