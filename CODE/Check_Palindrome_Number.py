def Check_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"


if __name__ == "__main__":
    print(Check_palindrome(121))
    print(Check_palindrome(1221))
    print(Check_palindrome(10))