# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/4 10:02
# 对象是字符串
for mylover in 'python': # 第一次取出来的是P,将p赋值给mylover，然后将item的值输出
    print(mylover)

# 对象是序列
for num in range(2,8,3): # 输出不包括终点的8
    print(num)

# 如果在循环体中不需要用到自定义变量，可将自变量写为“_”
a=0
sum=0
for a in range(5): # 计算0-5的累加和
    a+=1
    sum+=a
print('1-5之和为',sum)

# for in 计算1-100内的偶数和
sum=0
for item in range(0,101,2):
        sum+=item
print('使用for in循环计算0-100的偶数和',sum)

# for in 计算1-100内的奇数和
sum=0
for item in range(1,101):
    if item%2==1:
        sum+=item
print('使用for in循环计算0-100的奇数和',sum)

# for in计算能1-100内被3整除的数之和
sum=0
for _ in range(0,11):
    if _%3==0:
        sum+=_
print('0-11以内能被3整除的数之和为',sum)