# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/8/30 15:23
# 变量
name='mary' # 变量名+赋值运算符+值
name='mike' # 多次赋值后，变量名会指向新的空间
print(name)

name='mary'
print(name)
name='lucy'
print(name)

# 变量=标识+类型+值
print('标识',id(name))
print('类型',type(name))
print('值',name)
