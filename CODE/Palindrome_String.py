
def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    text = input("Enter a string: ")
    if is_palindrome(text):
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')
