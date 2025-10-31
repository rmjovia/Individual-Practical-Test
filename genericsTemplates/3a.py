from functools import reduce

numbers = [2,5,8,11,14,17,20]

#1 Use map() to square each number

squares = list(map(lambda x: x ** 2, numbers))
print ("Squares:", squares)

#2 Use filter() to select only squares > 100

filtered = list(filter(lambda x : x > 100, squares))
print ("Squares greater than 100:", filtered)

#3 Use reduce() to compute the sum of remaining numbers

total  = reduce(lambda a, b: a + b, filtered)
print ("Sum of the filtered squares:", total)