#6. Write a Python program to square and cube every number in a given list of integers using Lambda.
#Original list of integers:
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square=list(map(lambda a:a**2,x))
print(square)
cude=list(map(lambda a:a**3,x))
print(cude)

