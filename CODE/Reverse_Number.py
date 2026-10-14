def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse


if __name__ == "__main__":
    print(reverse_number(1234))
    print(reverse_number(567))
    print(reverse_number(120))