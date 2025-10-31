# Demonstrates use of the string_tools module.


import string_tools  

text = input("Enter a text: ")

# Use functions from string_tools
vowel_count = string_tools.count_vowels(text)
palindrome_status = string_tools.is_palindrome(text)

# Display results
print(f"\nNumber of vowels: {vowel_count}")
if palindrome_status:
    print("The text IS a palindrome.")
else:
    print("The text is NOT a palindrome.")
