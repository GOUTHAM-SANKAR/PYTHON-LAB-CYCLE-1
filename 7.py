'''Convert the seconds to hours : minute : seconds'''

#Enter the seconds to be converted
S=int(input("Enter the seconds to be converted"))

#Seconds to Hour
H=(S/3600)
#Seconds to Min
M=(S/60)
#Seconds to Remaining 
S1=(S%3600)

#Rounding decimals to integer
x=round(H)
y=round(M)
z=round(S1)

#print the result
print(x,":",y,":",z)