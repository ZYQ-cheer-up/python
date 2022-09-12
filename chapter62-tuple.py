# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 9:31
a=('lover','haters','helpless',222)
print(a,id(a),type(a)) #使用()

b=tuple((222,111,333))
print(b) #使用内置函数tuple()

#如果元组中只有一个元素，逗号也不能少
c=('lover',)
print(c,type(c))
#空列表的创建方式
lst=[]
lst1=list()
print('空列表',lst,lst1)
#空字典的创建方式
dict1={}
dict2=dict()
print('空字典',dict1,dict2)
#空元组的创建方式
tuple1=()
tuple2=tuple(())
print('空元组',tuple1,tuple2)