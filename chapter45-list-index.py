# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/7 9:02
lst=['hello',985,2.11,False,2.11]
print(lst.index(False))
print(lst.index('hello'))
print(lst.index(2.11)) #如果列表中有相同元素，只返回列表中相同元系的第一个元素的索引
#print(lst.index('python')) #如果查询的元素在列表中不存在，就会抛出ValueError
print(lst.index(2.11,3,5)) #索引范围不包括终点5