# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/9 15:28
lst=[996,985,211,3.14,777,434,211]
#调用列表对象的sort方法
print('before',lst,id(lst))
lst.sort() #默认升序排列
print('later',lst,id(lst)) #没有产生新的对象
lst.sort(reverse=True) #降序排列
print(lst)
lst.sort(reverse=False)
print(lst)
print()
#使用内置函数sorted()，会产生一个新的列表
lst1=[1,2,3,4,555,6666,77777,1,23,4,2435,123]
print(lst1,id(lst1))
lstnew=sorted(lst1)
print(lstnew,id(lstnew)) #sorted()产生了一个新的列表
lst2=sorted(lstnew,reverse=True)
print(lst2,id(lst2)) #sorted()产生了一个新的数组
# sort()不产生新的列表，sorted()产生新的列表，标识发生变化