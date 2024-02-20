# use range() function to tell python to skip numbers in a given range
# List of even numbers between 1 and 10:
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# range() format - range(start, stop, step)

# generate even numbers between 40 and 60 
even = list(range(40, 60, 2))
print(even)

# odd numbers: use the third argument of the range() function to make a list of the odd numbers from 1 to 20.
# use a for loop to print each number
odd_numbers = []
for odd in range(1,20,2):
    print(odd)
    odd_numbers.append(odd)

print(odd_numbers)
