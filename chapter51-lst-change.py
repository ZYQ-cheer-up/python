# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/9 14:51
#列表元素的修改操作
#按照索引一次修改一个值
lst=[996,985,211,3.14,'killers','在意什么']
print(type(lst),id(lst))
lst[4]=168
print(lst)
print(type(lst),id(lst)) #增加、减少或者修改成其他元素都不会改变原有列表的id
lst[2:5]=[2,4,5,6,7,2,5,3,2,1] #修改列表中的多个值
print(lst)
lst[3:7:2]
print(lst[3:7:2])