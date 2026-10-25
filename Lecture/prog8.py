#Pattern Printing
n=int(input("Enter Number of rows : "))
for i in range(n):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()