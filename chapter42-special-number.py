# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/6 10:40
# 找出1000-10000内，个位数**3+十位数**3+百位数**3+千位数**3=itself
for a in range(1000,10001):
    c=a%1000%100%10 #个位数
    d=a//100%10 #百位数
    e=a//1000 #千位数
    f=a//10%10
    if c**5+d**5+e**5+f**5==a:
        print(a)