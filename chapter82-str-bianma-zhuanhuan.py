# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/13 9:12
#编码：将字符串转换为二进制（byte），解码：将二进制转换为字符串
#编码 byte=str.encode(encoding='UTF-8/GBK')
s='海内存知己'
print(s.encode(encoding='GBK')) #在GBK这种编码中，一个中文占两个字节
print(s.encode(encoding='UTF-8')) #在UTF-8这种编码中，一个中文占三个字节
print()
#解码 str=byte.decoding(encoding='UTF-8/GBK')
#byte表示一个二进制数据（字节类型的数据
byte=s.encode(encoding='UTF-8') #编码，encoding
print(byte)
print(byte.decode(encoding='UTF-8')) #解码，decoding
print()
byte=s.encode(encoding='GBK') #编码，encoding
print(byte)
print(byte.decode(encoding='GBK')) #解码，decoding