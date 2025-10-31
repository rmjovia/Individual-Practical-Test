# Contains reusable string utility functions.


def count_vowels(text):
    """Counts the vowels (a, e, i, o, u) in the given text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def reverse_string(text):
    """Reverses and returns the given string."""
    return text[::-1]
