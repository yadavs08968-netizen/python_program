
def Factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

print(Factorial(5))
print(Factorial(4))
print(Factorial(0))
