# simple statistics with a list
# few python functions are helpful when working with lists of numbers
digits = [1,2,3,4,5,6,7,8,9,10]

minimum_digit = min(digits) # the minimum number
print(minimum_digit)

maximum_digit = max(digits) # the maximum number
print(maximum_digit)

total = sum(digits) # sum of the list digits
print(total)

# try it yourself 
# Make a list of the numbers from 1 to 1000, and then use a for loop to print the numbers
numbers_list = []
for number in range(1,1001):
    print(number)
    numbers_list.append(number)

print(numbers_list)

# prove that your lists starts at 1 and ends at 1000
max_number = max(numbers_list)
print(max_number)

min_number = min(numbers_list)
print(min_number)

# calculate the sum
total = sum(numbers_list)
print(total)
