# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/8 16:24
lst=[985,211,3.14,'好好学习，天天向上','haters','lover',3+4]
print(lst)
lst1=[1,2,3,4,7,6,9,4,5]
print(lst1)
lst[::]
#根据索引获取列表中的单个元素
print(lst[3])
#根据索引获取列表中的多个元素
print(lst[2:5:2])
#查询列表中元素的有无
print(777 not in lst)
print(999 in lst)
#列表元素的遍历
for _ in lst:
    print(_)
#列表添加单个元素
lst.append(731)
print(lst)
#列表添加至少一个元素
lst.append(lst1)
print(lst)
lst.extend(lst1)
print(lst)
#插入元素
lst.insert(3,996) #在列表第三个元素后面添加996
print(lst)
#切片
lst[3::]=lst1 #替换操作
print(lst)
#[]内部的表示索引对应元素，（）的标识第几个元素
#删除某个指定元素
lst.remove(4)
print(lst)
#按照索引删除元素
lst.pop(4)
print(lst)
#切片
lstnew=lst[1:6]
print('原本的列表',lst)
print('修改后的列表',lstnew) #形成了新的列表对象
lst[1:6]=[]
print(lst)