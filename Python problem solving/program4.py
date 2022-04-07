def print_pyramid(n):
    """Print a symmetrical pyramid of numbers descending from n"""


    bottom = []
    for j in range(n):
        row = [max(i, j + 1) for i in range(1, n + 1)]
        row = row[::-1][:-1] + row
        bottom.append(row)

    rows = bottom[::-1][:-1] + bottom


    for row in rows:
        row_str = [str(i) for i in row]
        print(f"{' '.join(row_str)}")
n = int(input("Enter the number: "))

print_pyramid(n)