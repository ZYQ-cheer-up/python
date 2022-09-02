# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/1 15:31
# 比较运算符,运算结果为布尔类型
a,b=10,40
print('a>b？',a>b)
print('a<b？',a<b)
print('a<=b?',a<=b)
print('a>=b?',a>=b)
print('a!=b?',a!=b)
print('a==b?',a==b)
# 一个=称为赋值运算符，两个==称为比较运算符变量由三部分组成，标识id，类型type，值value，==比较对象的值

# 比较对象的标识用is
a=996
b=996
print(a==b) #a,b值相等
print(id(a),id(b))
print(a is b) #比较a,b的标识是否一样

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2) #比较lst1,lst2的值是否一样
print(id(lst1),id(lst2)) #比较lst1,lst2的标识是否一样
print(lst1 is lst2) #比较lst1,lst2的标识是否一样

print(a is not b) #比较a,b的标识是否不同
print(lst1 is not lst2) #比较lst1,lst2的标识是否不同