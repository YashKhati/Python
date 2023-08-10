def SelectionSort(arr,n):
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        (arr[i] , arr[min_index]) =(arr[min_index] , arr[i])

arr = []
n = int(input("Enter size of list : "))

print("Enter List Elements  : ")
for i in range (0,n):
    arr.append(int(input()))    

SelectionSort(arr,n)

print("Sorted Array : ")
print(arr)
