# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/13 8:45
#格式化字符串
#格式化字符串的第一种方式
#占位符
name='钟英群'
age=25
print('我叫%s,今年%d岁'%(name,age))
print()
#%s字符串，%d整数
#花括号{}
print('my name is {0},i am {1} years old'.format(name,age))
print()
#f-string
print(f'my name is {name},i am {age} years old')