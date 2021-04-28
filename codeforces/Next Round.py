li = input().split()
n,k = int(li[0]), int(li[1])
mark = [int(x) for x in input().split()]
count = 0
k_mark = mark[k-1]

for i in mark:
    if i >= k_mark and i != 0:
        count += 1
print(count)
