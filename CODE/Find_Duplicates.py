def find_duplicates(numbers):
    duplicates = []
    for x in numbers:
        if numbers.count(x) > 1 and x not in duplicates:
            duplicates.append(x)
    return duplicates


numbers = [1, 2, 3, 4, 2, 5, 3]
print("Duplicates:", find_duplicates(numbers))
