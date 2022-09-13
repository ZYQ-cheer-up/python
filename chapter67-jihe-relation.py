# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 14:57
#判断集合是否相等,元素相同就像等
s1={11,22,33,44,55,1,2,34,7,5,6}
s2={1,2,34,7,5,6}
print(s1==s2)
print(s1!=s2)
print()
#一个集合是否是另一个集合的子集si.issubset(s2)
print(s2.issubset(s1))
s3={231,3123,13,123,123,23}
print(s3.issubset(s1))
print()
#一个集合是否是另一个集合的超集s1.issuperset(s2)
print(s1.issuperset(s2))
print(s1.issuperset(s3))
print()
#一个集合与另一个集合是否无交集s1.isdisjoint(s2)
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))