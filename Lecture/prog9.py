#Pattern Printing
n=int(input("Enter Number of rows : "))
num=0
for i in range(n):
    for j in range(i):
        print(chr(65+num), end=" ")
        num+=1
    print()