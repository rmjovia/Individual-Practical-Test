# Demonstrates importing and using functions from utils package.


from math_utils import factorial, gcd, fibonacci
from string_utils import count_vowels, reverse_string

#  math_utils
print("  Math Utilities ")
print("Factorial of 5:", factorial(5))
print("GCD of 20 and 12:", gcd(20, 12))
print("Fibonacci sequence (first 6 terms):", fibonacci(6))

# string_utils
print("\n   String Utilities  ")
text = "Hello World"
print(f"Text: {text}")
print("Vowel Count:", count_vowels(text))
print("Reversed String:", reverse_string(text))
