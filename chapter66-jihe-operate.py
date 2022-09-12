# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 10:33
#集合的相关操作
#判断
set1={123123,312312,13123,4123,12312341,1313}
print(1313 in set1)
print(111 in set1)
print(123123 not in set1)
#增加
set1.add(996) #增加单个元素
print(set1)
set1.update({31321,212,4124124,'asdad'}) #增加至少一个元素
print(set1)
set1.update(['dqadqwdw',213123,'dqwdwqd',123123])
print(set1)
set1.update(('daqdwqd',21313,'dadasd',23123213))
print(set1)
set1.update(range(7))
print(set1)
print()
#集合的删除操作
set1.remove(0)
print(set1)
#set1.remove(213213) print(set1) KeyError: 213213
set1.discard(213123)
print(set1) #不存在也不会抛出异常
set1.pop()
#set1.pop(3) TypeError: set.pop() takes no arguments (1 given),不能指定参数
print(set1)
set1.clear()
print(set1) #清空集合中的元素