# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 18:29
#设置宽度小于原字符串，则返回原字符串
s1='hello,Python'
print(s1.center(20,'*')) #居中对齐，填充符设置为‘*’
print(s1.ljust(20,'*')) #左对齐，填充符设置为‘*’
print(s1.ljust(30,'+')) #左对齐，填充符设置为‘+’
print(s1.ljust(40)) #左对齐，填充符未设置，默认为为‘ ’
print()
print(s1.rjust(25,'/'))
print(s1.rjust(25))
print(s1.rjust(30))
print()
print(s1.zfill(20)) #右对齐，左边用0填充
print(s1.zfill(10))
print('-9987'.zfill(8))