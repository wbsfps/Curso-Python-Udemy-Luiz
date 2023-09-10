lines_and_columns = [
    (x, y)
    if y != 2 else (x, y * 2000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]

print(lines_and_columns)
