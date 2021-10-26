Arr = [78, 32, 11, 1, 0, 44, 55]

print('Before sort')
print(Arr)
for i in range(len(Arr)-1):
    for j in range(len(Arr)-1-i):
        temp = 0
        if Arr[j] > Arr[j+1]:
            temp = Arr[j]
            Arr[j] = Arr[j+1]
            Arr[j+1] = temp

print('After sort')
print(Arr)