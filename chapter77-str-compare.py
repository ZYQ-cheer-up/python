# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 20:03
#字符串的比较操作：<,>,<=,>=,==,!=
print('apple'>'app') #True
print('apple'>'banana')
print(ord('a'),ord('b')) #比较原始值的大小
print()
print(chr(98),chr(97))
print(chr(101))
print(ord('钟'))
print(ord('杨'))
print()
#==与is 的区别，==比较的是值value，is比较的是id
a=b='Python' #True
c='Python' #True
print(a==b,b==c) #True
print(a is b,b is c) #True
print(id(a),id(b),id(c))