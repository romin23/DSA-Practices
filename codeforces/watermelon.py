def watermelon(kg):
    if kg % 2 == 0 and kg != 2:
        return 'YES'
    # elif kg > 3:
    #     return 'YES'
    else:
        return 'NO'
    

kilo = int(input())
print(watermelon(kilo))