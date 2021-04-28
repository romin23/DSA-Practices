for i in range(int(input())):
    w = input()
    if len(w) > 10:
        print (w[0] + len(w)-2 + w[-1])
    else:
        print(w)