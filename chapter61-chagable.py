# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 9:24
#可变序列
lst=[2121,123,3213,34143,1324,1321]
print(id(lst))
lst.append(2424)
print(id(lst)) #增删改操作不改变id的元素，列表称为可变序列
s='super'
print(id(s))
s=s+'star'
print(id(s)) #字符串在增删改操作过后id发生了变化