p = '11,22'
print(type(eval(p)))
for i, v in enumerate(eval(p)):
    print(i, v)