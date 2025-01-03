"""
Task 2: Counting Word Occurrences
You are given a list of words. You need to create a dictionary where the keys are words and the values are the number of times each word occurs in the list.
Use the `get()` method to check if the word already exists in the dictionary, and if it does, increment its value.

Input:
- A list of words (strings).

Output:
- A dictionary where the keys are words and the values are the number of occurrences of each word.

Example:
Input:
    words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
Output:
    {'apple': 2, 'banana': 3, 'orange': 1}
"""
if __name__ == "__main__":
    n = input('Enter Sentence:')

    # check if input is empty or spaces only
    if not n:
        raise ValueError('The input message can not be empty or consist of spaces only!')

    # split sentence to words separated by space
    words = n.split()

    # empty dict to store the words
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print(word_count)