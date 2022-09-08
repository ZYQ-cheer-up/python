# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/8 15:39
# 列表元素的增加元素
# 向列表的末尾增加一个元素，append
lst=[996,700,985,211,3.14,'haters','lover']
print('添加元素之前',lst,id(lst),type(lst))
lst.append(731)
print('添加元素之后',lst,id(lst),type(lst)) #添加元素之后没有创建新的列表，添加新元素之后的列表id没有改变

# 向列表末尾至少添加一个元素，extend
lst1=[12345,'上山打老虎']
lst.append(lst1)
print(lst) #将lst1作为一个元素添加到lst末尾
lst.extend(lst1)
print(lst) #将lst1的元素添加到lst末尾

#在任意位置上添加一个元素，insert
lst.insert(4,'在第四个元素后面插入')
print(lst)

#在任意位置上添加至少一个元素，切片
lst3=[111,222,3.22,'天天学习好好向上','lover']
lst[1::]=lst3 #把第一个元素往后的元素删去，将lst3中的元素加入
print(lst)