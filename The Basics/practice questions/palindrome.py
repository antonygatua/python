"""
Check if a given string is a palindrome.

A palindrome is a word, phrase, number, or other sequence of characters
that reads the same backward as forward (ignoring case and spaces). 

Steps:
    1. Take input from the user as a string.
    2. Normalize the string by converting it to lowercase and removing spaces.
    3. Check if the normalized string is the same when reversed.
    4. Print whether the input string is a palindrome or not.

Example:
    Input: "Racecar"
    Output: "The string is a palindrome."

    Input: "Hello"
    Output: "The string is not a palindrome."
"""

word = input("Enter string to check if palindrome: ").lower().replace(" ", "")

# check if palindrome
if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")