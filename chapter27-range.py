# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/2 9:39
# range()的三种创建方式
# range(a),a为integer,range(终值)
a=range(8)
print(a) # rangr(0,8)，默认相差步长为1，从零开始，到八结束，但是不包括八
print(list(a)) #用于查看range对象中的整数序列

# range(a,b)，a,b为integer，range(初值，终值)
a=range(1,8) # 设定从一开始，到八结束，但是不包括八，沿用默认步长为一
print(a)
print(list(a))

# range(a,b,c)，range(初值，终值，步长)
a=range(1,10,2)
print(list(a))
b=range(1,10,3)
print(list(b))

#判断指定整数在序列中是否存在'in ,not in'
print(7 in b)
print(10 not in b)
print(9 in b)