
def fibonacci(num):
    a = 0
    b = 1
    series = []
    for i in range(num):
        series.append(a)
        c = a + b
        a = b
        b = c
    return series

print(fibonacci(5))
print(fibonacci(7))
