
def Sum_Of_Digits(num):
    total = 0
    num = abs(num)

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    return total


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The sum of digits of {num} is: {Sum_Of_Digits(num)}")
