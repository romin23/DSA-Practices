def scale(n,x,gold_weight):
    gold_weight.sort()
    left = []
    c = ' '
    add = 0
    new = []
    last = len(gold_weight) -1
    if len(gold_weight) == 1 and gold_weight[0] == x:
        print('NO')
        return
    
    for i in gold_weight:
        add += i
        if add == x:
            add -= i
            left.append(i)
        else:
            new.append(i)
    summ = sum(new+left)
    if summ != x  :  
        print('YES')
        for i in new + left:
            print(i,end = ' ')
        print()
    else:
        print('NO')

t = int(input())

for i in range(t):
    tc_bp = [int(x) for x in input().split()]
    n,x = tc_bp[0],tc_bp[1]
    gold_weight = [int(x) for x in input().split()]
    scale(n,x,gold_weight)
