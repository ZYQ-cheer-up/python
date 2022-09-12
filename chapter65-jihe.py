# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 10:11
#集合的创建
a={'haters':100,'lover':1}
b={2131,2,1,1,23,3,442,5,5,6,7,4,45,1}
print(a,type(a))
print(b,type(b)) #集合中的元素不允许重复
c=set((123,324,'12431','asdfa'))
print()
print(c)
#将列表，元组，集合转化为集合
set1=set([1,2,'3123','fsaf'])
set2=set((1313,412432,'dadsad'))
set3=set({'qaedaqd',123,2131,123,2131,'人才'})
#集合元素是无序的
print()
print(set1,type(set1))
print()
print(set2,type(set2))
print()
print(set3,type(set3))
print()
set4=set(range(4))
print(set4,type(set4))
print()
set5=set('killers')
print(set5,type(set5))
print()
#定义一个空集合
set6={}
print(set6)
print(type(set6))
set7=set()
print(type(set7))