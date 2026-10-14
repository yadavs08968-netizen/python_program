
def remove_duplicates(numbers):
    unique_numbers = list(dict.fromkeys(numbers))
    return unique_numbers


if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 4, 1, 5]
    result = remove_duplicates(numbers)
    print(result)
