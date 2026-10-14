def find_missing(numbers):
    n = len(numbers) + 1
    for i in range(1, n + 1):
        if i not in numbers:
            return i

numbers = [1, 2, 4, 5]
print("Missing number:", find_missing(numbers))
