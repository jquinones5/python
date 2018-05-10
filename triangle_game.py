print("Welcome to the Game of Triangle!")
rows = input("Enter a number of rows for the triangle:  ")
while True:
    if rows.isdigit():
        if int(rows) > 0:
            rows = int(rows)
            break
        else:
            print("Please input a positive non-zero number.")
            rows = input("Enter a number of rows for the triangle:  ")
    else:
        print("Please input an integer number.")
        rows = input("Enter a number of rows for the triangle:  ")
triangle = [""]
for n in range(1,rows + 1):
    triangle.append("")
    triangle[n] = " " * (rows - n)
    triangle[n] += "x" * n
    triangle[n] += "x" * (n - 1)
    print(triangle[n])
