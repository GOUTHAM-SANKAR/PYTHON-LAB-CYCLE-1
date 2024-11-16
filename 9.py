'''Swap 2 numbers without using a temporary variable.'''

#Input X and Y 
x = int(input("The first number is:"))
y = int(input("The second number is:"))

#Swapping without using temporary variable
x = x + y
y = x - y
x = x - y

#Printing the result
print('The value of x after swapping:',x)
print('The value of y after swapping:',y)