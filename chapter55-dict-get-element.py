# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/9 16:43
# 获取字典中的元素
dict1={'haters':10,'lover':100,'天书奇谈':10000}
print(dict1['lover']) #使用[]
print(dict1.get('天书奇谈')) #使用get()
#print(dict1['999']) KeyError: '999'
print(dict1.get(996))
print(dict1.get('一生所爱','she')) #'she'是在查找‘一生所爱’这个键的value不存在时，提供的一个默认值