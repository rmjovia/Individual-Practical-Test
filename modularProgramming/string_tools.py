# string_tools.py
# A reusable module for basic string operations.
# Functions: count_vowels(text)
#            is_palindrome(text)


def count_vowels(text):
    """
    Counts the number of vowels (a, e, i, o, u) in a string.
    This function is case-insensitive.
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def is_palindrome(text):
    """
    Checks whether the provided text is a palindrome.
    Ignores spaces and capitalization.
    Example: "Race car" → True
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
