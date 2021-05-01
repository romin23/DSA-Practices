
for i in range(1,6):
    row = input().split()
    if '1' in row:
        row_idx = i
        col_idx = row.index('1') + 1
        break

print(abs(3-row_idx) + abs(3-col_idx))
