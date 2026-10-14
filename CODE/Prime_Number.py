def check_prime(num):
    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"

    return "Prime"

print(check_prime(7))
print(check_prime(10))