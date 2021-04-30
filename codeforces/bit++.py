n = int(input())
X = 0
for i in range(n):
    eXp = input()
    if eXp == '++X' or eXp == 'X++':
        X += 1
    elif eXp == '--X' or eXp == 'X--':
        X -= 1
print(X)