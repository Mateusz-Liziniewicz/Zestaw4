def factorial(n):
    for i in range(n+1):
        if(i==0):
            silnia = 1
        else:
            silnia *= i
    return silnia;

silnia1 = factorial(5)
silnia2 = factorial(10)
silnia3 = factorial(15)
print(f"{silnia1}\n{silnia2}\n{silnia3}")