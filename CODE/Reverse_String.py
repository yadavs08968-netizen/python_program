
def reverse_string(s):
    reverse = ""
    for char in s:
        reverse = char + reverse
    return reverse


if __name__ == "__main__":
    string = input("Enter a string: ")
    print("Reversed string:", reverse_string(string))
