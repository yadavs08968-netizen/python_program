
def count_frequency(text, char):
    count = 0
    for ch in text:
        if ch == char:
            count += 1
    return count


if __name__ == "__main__":
    text = input("Enter a string: ")
    char = input("Enter a character to count its frequency: ")
    frequency = count_frequency(text, char)
    print(f"The character '{char}' appears {frequency} times in the string.")
