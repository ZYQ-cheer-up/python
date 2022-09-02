# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/1 10:02
# 赋值运算符，运算顺序从右到左
j=985+211
print(j)

# 链式赋值
a=b=c=996
print(a,id(a),b,id(b),c,id(c))
a=985

# 参数赋值
a+=211 #就是a=a+211
print(a)
a-=996 #就是a=a-996
print(a)
a*=2 #就是a=a*2
print(a)
a/=3
print(a)
a//=2
print(a)

#解包赋值
a,b,c,d=985,996,211,7
print(a,b,c,d)
print (a,id(a),type(a))

# 交换两个变量的值
a,b=10,40
print("交换之前",a,b)
#交换
a,b=b,a
print('交换之后',a,b)