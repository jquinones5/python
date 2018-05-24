"""Calculates the sum of a numbers digit"""
integer = int(input("Enter an integer: "))
found_n = False
x = integer
n = 1
while not found_n:
    if x < 10:
        found_n = True
    else:
        x = x / 10
        n += 1
total = 0
for num in range(0,n):
    total += integer % 10
    integer = int(integer / 10)
print(total)
