def fuc(int1, int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply

print(fuc(3,2))  #tuple return kr rha ye
add, multiply  = fuc(3,2)
print(add, multiply)
