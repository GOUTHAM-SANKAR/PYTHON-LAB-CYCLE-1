'''Swap 2 numbers using a temporary variable'''

#Input X and Y 
X = int(input("The first number is:"))
Y = int(input("The second number is:"))

#Swapping using Temporary Variable
temp = X
X = Y
Y = temp

#Printing after Swapping
print('The value of X after swapping:',X)
print('The value of Y after swapping:',Y)
