#factors(n)

lower=input("Enter lower limit")
upper=input("Enter Upper limit")

n=input("Enter the divisor")

for i in range(lower,upper+1):
    if(i%n==0):
       print(i)