# 内蒙古工业大学
# 硕士研究生
# 钟英群
# 开发时间：2022/9/6 9:18
a=0
b=0
while a<4: #最多点餐四份
    pdd = input('order you food')
    if pdd=='hmj':
        a+=1
        b+=15
        print('ordering')
        continue
    elif pdd=='jgb':
        a+=1
        b+=25
        print('ordering')
        continue
    else:
        print('please order food our restaurant have')
        continue
print(b)