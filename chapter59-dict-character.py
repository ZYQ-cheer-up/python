# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/11 16:42
a={'name':110,"name":120}
print(a) #key不允许重复，不报错但会发生覆盖

b={'order':25,'age':25}
print(b) #value允许重复，且不会发生覆盖

c=[10,20,30]
c.insert(2,996) #将此元素变成列表中索引为2的元素
print(c)
#d={c:99} TypeError: unhashable type: 'list' print(d)
