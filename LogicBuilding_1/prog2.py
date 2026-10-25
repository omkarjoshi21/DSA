# Get the smallest, second smallest, largest and second largest number in an array

arr = [10, 8, 3, 4, 88, 34, 72]

min = arr[0]
max = arr[0]
smin = arr[0]
smax = arr[0]

for num in arr:
    if num > max:
        smax = max
        max = num
    elif num > smax and num != max:
        smax = num

    if num < min:
        smin = min
        min = num
    elif num < smin and num != min:
        smin = num

print("Smallest number is:", min)
print("Second smallest number is:", smin)
print("Largest number is:", max)
print("Second largest number is:", smax)