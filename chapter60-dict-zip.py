# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/12 9:15
items=['fruit','book','others']
prices=[96,65,43,56464,66]
d={item.upper():price for item,price in zip(items,prices)}
print(d)