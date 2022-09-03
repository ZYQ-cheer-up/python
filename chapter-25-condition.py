# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/2 9:02
# 要求从键盘输入两个整数，并且比较大小
a=int(input('请输入第一个整数'))
b=int(input('请输入另一个整数'))
'''if a<b:
    print(a,'小于',b) # 换成print（str（a）+'小于'+str(b))结果输出比较好看
elif a>b:
    print(a,'大于',b)
else:
    print(a,'等于',b)常规写法'''
print('使用条件表达式进行比较')
print(str(a)+'小于等于'+str(b) if a<=b else str(a)+'大于'+str(b))