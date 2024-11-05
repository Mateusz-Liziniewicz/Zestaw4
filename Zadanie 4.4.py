def fibonacci(n):
    result = []
    for i in range(n+1):
        if(i==0):
            result.append(i)
        else:
            if(i==1):
                result.append(i)
            else:
                result.append(result[i-1] + result[i-2])
    return result[n]
result1 = fibonacci(10)
result2 = fibonacci(20)
result3 = fibonacci(30)
result4 = fibonacci(2115)
print(result1)
print(result2)
print(result3)
print(result4)