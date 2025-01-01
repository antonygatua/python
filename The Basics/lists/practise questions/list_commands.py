"""
Perform operations on a list based on input commands.

The commands to handle are as follows:
1. insert i e: Insert integer e at position i.
2. print: Print the current state of the list.
3. remove e: Remove the first occurrence of integer e from the list.
4. append e: Append integer e to the end of the list.
5. sort: Sort the list in ascending order.
6. pop: Remove the last element of the list.
7. reverse: Reverse the list.

Input:
- The first line contains an integer, N, the number of commands.
- The next N lines each contain one of the commands described above.

Output:
- For every print command, output the current state of the list.

Example:
Input:
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

Output:
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
"""

def main():
    n = int(input())

    # Initialize an empty list
    results = []

    for i in range(n):
        query = input().split()

        if query[0] == 'insert':
            # Insert at index
            index, value = int(query[1]), int(query[2])
            results.insert(index, value)

        elif query[0] == 'print':
            # Print the list
            print(results)

        elif query[0] == 'remove':
            # Remove first occurrence of the element
            results.remove(int(query[1]))

        elif query[0] == 'append':
            # Append integer at the end of the list
            results.append(int(query[1]))

        elif query[0] == 'sort':
            # Sort the list in ascending order
            results.sort()

        elif query[0] == 'pop':
            # Remove the last item in the list
            results.pop()

        elif query[0] == 'reverse':
            # Reverse the list
            results.reverse()

        else:
            # This case is not required as per the problem description
            print('Wrong operation')


if __name__ == "__main__":
    main()