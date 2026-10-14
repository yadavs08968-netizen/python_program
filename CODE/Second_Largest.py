
def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort()
    return unique_numbers[-2]


if __name__ == "__main__":
    numbers = list(map(int, input(
        "Enter a list of numbers separated by spaces: "
    ).split()))

    result = second_largest(numbers)

    if result is not None:
        print(f"The second largest number is: {result}")
    else:
        print("Not enough unique numbers to determine the second largest.")
