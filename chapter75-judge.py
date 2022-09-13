# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 19:08
#判断字符串是否为合法标识符 isidentifier()
s='hello,my lover'
print('1,',s.isidentifier()) #False
print('2,','hello'.isidentifier()) #True
print('3,','张三'.isidentifier()) #True
print('4,','王老五——'.isidentifier()) #Fdalse
print('5,','hello_'.isidentifier()) #True
print('6,','hello_996'.isidentifier()) #True
print()
print('7,','\t'.isspace()) #True，确实是空白字符
print()
print('8,','asdfghjk'.isalpha()) #True
print('9,','张三'.isalpha()) #False,python左下角可以设定编码方式，utf-8，英文字母，汉字，假名，西里尔字母都判定为alpha
print('10,','张三-'.isalpha()) #False
print()
print('11,','1231414'.isdecimal()) #True
print('12,','1231414啦啦啦'.isdecimal()) #False
print('13,','three'.isdecimal()) #False
print()
print('14,','1231414'.isnumeric()) #True
print('15,','1231414---'.isdecimal()) #False
print('16,','1231414啦啦啦'.isdecimal()) #False
print()
print('17','awedawe1'.isalnum()) #True
print('18','zhang三111'.isalnum()) #True
print('19','asd231张！'.isalnum()) #False