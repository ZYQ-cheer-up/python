# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/7 9:14
#步长为正数
lst=['hello',985,3.14,211,'hello',996]
print(lst[-4]) #希望获取索引为-4的元素
lst1=['hello',985,3.14,211,'my','lover',996,700]
print(lst1[0:6:2]) #print(lst[start:stop:step])，不包括终点
print(lst1[0:7:3])
print('original list',lst1,id(lst1),type(lst1))
print('part list',lst1[0:7:3],type(lst1[0:7:3]),id(lst1[0:7:3])) #切片的列表形成了一个新的列表
print(lst1[2:6]) #默认步长为1
print(lst1[2:6:])
print(lst1[2:6:2])
print(lst1[:7:]) #省略起点默认为0开始
print(lst1[::]) #终点不写默认为到最后一个元素
#步长为负数
print(lst1[::-2]) #步长为负数，默认起点为最后一个元素，终点为第一个元素
print(lst1[7:0:-3]) #步长为负数同样，包括起点，不包括终点，想包括终点只有空开
print(lst1[7::-1])