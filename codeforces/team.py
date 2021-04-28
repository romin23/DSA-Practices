count = 0
for i in range(int(input())):
    q = input().split()
    
    # print(q)
    if (int(q[0]) == 1 and int(q[1]) == 1) or (int(q[2]) == 1 and int(q[1]) == 1) or (int(q[0]) == 1 and int(q[2]) == 1):
        count += 1
print(count)