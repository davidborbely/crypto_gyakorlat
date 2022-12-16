mult = 1


for i in range(366, 343, -1):
    mult *= i

print(mult/(366**23))