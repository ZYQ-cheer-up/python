# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/8/30 16:30
#浮点类型，浮点数由整数部分和小数部分组成
a=3.14
print(a,id(a),type(a))
n1=1.1
n2=2.2
print(n1+n2) #浮点数存储不精确，解决方案，导入decimal模块
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))