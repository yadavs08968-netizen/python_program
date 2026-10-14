
def check_vowel_consonant(char):
    if len(char) != 1 or not char.isalpha() or not char.isascii():
        return "Invalid"

    if char.lower() in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"


if __name__ == "__main__":
    char = input("Enter a character: ")
    print(check_vowel_consonant(char))
