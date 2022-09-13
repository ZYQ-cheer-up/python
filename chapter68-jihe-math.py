# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 15:13
s1={11,22,33,44,55,66}
s2={11,2,3,4,5,8,7,7}
s3={211,985,731,250,877,996,222}
s4={996,985,211}
#取交集
print(s1.intersection(s2))
print(s3.intersection(s4))
print(s3 & s4)
print(s1)
print(s2)
print(s3)
print(s4)
print() #s1.interseciont(s2)==s1 & s2
#取并集
print(s1.union(s2))
print(s3.union(s4))
print(s1 | s2)#s1.union(s2)==s1 | s2
print(s1)
print(s2)
print(s3)
print(s4)
print()
#差集
print(s1.difference(s2))
print(s2.difference(s1))
print(s3-s4)
print(s4-s3)#s1.difference(s2)==s1-s2
print(s1)
print(s2)
print(s3)
print(s4)
print()
#对称差集
print(s1.symmetric_difference(s2))
print(s1^s2)#s1.symmetrivc_difference(s2)==s1^s2,各自独有元素的集合