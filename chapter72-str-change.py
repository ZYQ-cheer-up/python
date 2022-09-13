# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 16:38
#字符串的大小写转换
s1='hello,python'
a=s1.upper() #全部改写为大写
print(a)
print(id(s1),id(a))#2811131658160 2811131599408,转成大写后将会产生一个新的字符串对象
print()
b=s1.lower() #全部改写为小写
print(a,type(a),id(s1),id(a))
print(b,type(b),id(s1),id(b))
print()
print(s1==b)
print(s1 is b) #内容相同，地址不同，没有驻留
s2='FUCK the FUCKING world'
print(s2.swapcase()) #大小写发生反转
c=s2.swapcase()
print(id(c),id(s2))
print()
print(s2.title()) #首字母大写，其他的转换为小写
d=s2.title()
print(id(d),id(s2))
print()
e=s2.capitalize() #首字母改成大写，其它字符转换为小写
print(e,id(e),id(s2))