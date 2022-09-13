# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 20:27
#字符串是不可变类型，切片将产生新的对象
s='hello,Python'
s1=s[:5] #没有指定起始位置，从索引0开始切
print(s1) #没指定终点，所以切到最后
s2=s[6:]
print(s2)
s3='!'
s4=s1+s2+s3
print(s4)
print(id(s),id(s1),id(s2),id(s3),id(s4))
#切片，[start:end:step]
print(s[1:5:1])
print(s[3:8:1])