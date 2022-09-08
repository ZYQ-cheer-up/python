# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/8 15:29
# 判断列表元素的存在性
print('l' in 'lover')
print('h' not in 'killer')
print()

lst=[985,211,3.14,'haters']
print(985 in lst)
print(996 not in lst)
print(731 in lst)
print()

for _ in lst: #列表的遍历，将列表中的元素依次输出
    print(_)