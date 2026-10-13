
def fibonacci_series(num):
    a = 0
    b = 1
    series = []
    for i in range(num):
        series.append(a)
        c = a + b
        a = b
        b = c
    return series

print(fibonacci_series(5))
print(fibonacci_series(7))
