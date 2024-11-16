'''Area and perimeter of a triangle'''

#Importing Math module
import math

#Read the first Side
A=int(input("Enter the first Side: "))

#Read the second Side 
B=int(input("Enter the second Side: "))

#Read the third Side 
C=int(input("Enter the third Side:"))

#The Perimeter of the Triangle is
P=A+B+C

#The Semi perimeter of the Triangle is
S=P/2

#Assigning Math module
k=math.sqrt

#The Area of the Triangle is
T=(k(S*(S-A)*(S-B)*(S-C)))

#Area is
print("The area of the Triangle is:",T)
