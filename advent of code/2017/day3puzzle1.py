from math import *;
"""
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49 ..."""
val = 265149;
value = int(sqrt(val));
if(value % 2 == 0):
    value -= 1;
lines = ((value - 1) // 2) + 1;
first_in_line = value ** 2;
last_in_line = (value + 2) ** 2;
val_to_end = last_in_line - val;
steps = lines * 2 - val_to_end;

print(val);
print(lines);
print(first_in_line);
print(last_in_line);
print(steps);
