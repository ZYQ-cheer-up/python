# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/11 15:45
dict1={'lover':996,'killers':985,'haters':211,'ugrly':700,'3.14':456}
print(dict1)
print(dict1.keys()) #获取所有的键
print(dict1.values()) #获取所有的值
print(dict1.items()) #获取所有的键值对
print(type(dict1.items()),type(dict1.keys()),type(dict1.values))
keys=dict1.keys()
values=dict1.values()
items=dict1.items()
print(list(keys),type(list(keys))) #将所有键组成的视图转成列表
print(list(values),type(list(values))) #将所有值组成的视图转成表
print(list(items),type(list(items))) #将所有的键值对组成的视图转换为表