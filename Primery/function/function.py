def delitel(number):
    b = 0
    for i in range(1, number+1):
        if number % i == 0:
            b = b + 1
            print(i)
    return b