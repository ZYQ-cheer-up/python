# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/8/29 21:38

# ASC码，用计算器可以实现
print(chr(0b100111001011000)) # 0b表示二进制
print(ord('乘')) # 用十进制表示

import keyword # 保留字，给对象起名字不能用
print(keyword.kwlist)
# 保留字：['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# 标识符，变量、函数、类、模块、和其他对象起的名字就叫做标识符
# 规则，字母、数字、下划线；不能以数字开头；不能是保留字；严格区分大小写