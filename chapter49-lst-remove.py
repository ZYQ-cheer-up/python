# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/8 16:02
lst=[985,211,3.14,731,'haters','my lover',985]
lst.remove(985)
#lst.remove() #TypeError: list.remove() takes exactly one argument (0 given)
print(lst) #从列表中移除一个元素，如果有重复的元素，则只移除第一个元素
#lst.remove(333) #ValueError: list.remove(x): x not in list

#根据索引移除元素，pop()
lst.pop(3)
print(lst)
#lst.pop(444) #IndexError: pop index out of range
lst.pop() #pop()不指定索引，则移除列表当中最后一个元素
print(lst)

#切片，一次至少删除一个元素，将产生一个新的列表
lstnew=lst[1:3]
print('原本的列表',lst)
print('切片后的列表',lstnew)
#不产生新的列表对象，而是删除列表中的内容
lst[1:3]=[] #实际上是用空表格对列表内的元素进行替换
print(lst)

#清楚列表中的所有元素
lst.clear()
print(lst)

#删除列表对象
del lst
#print(lst) #被删除的的列表对象不存在了，无法打印