# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/11 10:44
dict1={'我的1992':100,'华尔街大亨':996,'闪闪的红星':985,211:375,}
dict2=dict(year=1937,place='beijing',thing='massacre')
print(dict1)
print()
print(dict2)
print('我的1992' in dict1)
print('year' not in dict2)

#删除字典元素
del dict1['我的1992'] #删除指定的键值对
print(dict1)
dict1.clear() #清空字典元素
print(dict1)

#新增字符元素
dict2['influence']='killing' #增加在最后的位置
print(dict2)
print()
dict3={'year':2022,'mouth':9,'day':11,'time':11,'people':3}
print(dict3)
dict3['relation']='mormal' #增加字典元素
print(dict3)
del dict3['year'] #删除字典元素
print(dict3)
dict3['relation']='close' #x修改建对应的值
print(dict3)
dict3.clear() #清空字典
print(dict3)