#Reverse the given number

n=input("Enter a number")
rev=0
temp=n
while(n>0):
     d=n%10
     rev=rev*10+d
     n=n//10

print("Reverse=",rev)

if(rev==temp):
  print("Palindrome")
else:
   print("Not a Palindrome")  