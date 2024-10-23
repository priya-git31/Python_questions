# take a list of 4 numbers and add 10 to each number and print

numbers = [2,3,4,5]
total = 0

for number in numbers: 
    total = total + number 
    print(total)


# take a list of 5 numbers and  print multiples of 10 for each numbers

numbers = [2,3,4,5,6]

for number in numbers:
    total = number * 5 
    print(total)

# take a list of 4 numbers and if the sum is even add 100 to the sum
# if the sum is odd 90 to it 
numbers = [2,3,4,5,6]

total = sum(numbers)

if total % 2 == 0: 
    print("total is even")
    print(total + 100)
else:
    print(total + 90)


# take a list of 6 numbers and get the sum of even numbers in the list
numbers = [33,34,27,23,18,19]

sum_even = 0
for number in numbers: 
    if number % 2 == 0:
        sum_even = number + sum_even
        print(sum_even)

          
# take a list of 6 numbers and get the sum of odd  numbers in the list
numbers = [7,10,3,4,9]

sum_odd = 0 

for number in numbers: 
    if number % 2 == 1: 
        sum_odd = number + sum_odd
        print(sum_odd)

# take a list of 4 numbers and get the sum of first and last numbers 
numbers = [2,34,44,4]

sum = 0 
for index, number in enumerate(numbers): 
    if index == 0 or index == 3:
        sum = sum + number
print(sum)

# take a list of 4 numebrs and pop the first letter and get the sum after that
numbers = [2,3,45,4]

popped = numbers.pop(0)

sum = 7

for number in numbers:
    sum = sum + number
print(sum)
