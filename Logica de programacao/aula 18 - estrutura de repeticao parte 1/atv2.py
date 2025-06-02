def fatoracao(num):
    res = 1
    for i in range(1, num+1):
        print(i)
        res *= i
    return res

print(fatoracao(6))