# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 16:25
#字符串的查询操作
str1='hello,hello'
print(str1.index('lo')) #3
print(str1.find('lo')) #3
print(str1.rindex('lo'))#9
print(str1.rfind('lo'))#9
#print(str1.index('j')) #ValueError: substring not found
print(str1.find('j'))
#print(str1.rindex('k')) #ValueError: substring not found
print(str1.rfind('k'))