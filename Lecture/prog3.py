#Pallindrome Number
num=int(input("Enter Number: "))
sum=0
n=num
while(n>0):
        sum=sum*10+n%10
        n=n//10

if(num==sum):
        print(num,"is a palindrome number")
else:
        print(num,"is not a palindrome number")