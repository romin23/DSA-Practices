def possible(num):
 
    if((num & (num - 1)) == 0):
        return 'YES'
    return 'NO'
 
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        num = int(input())
        print(possible(num))