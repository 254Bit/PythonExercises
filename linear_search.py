# Linear Search is a sequential search algorithm that starts at one end and goes through each element of a list 
# until the desired element is found,
# otherwise the search continues till the end of the data set.

def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [4,2,1,7,5]
x = 7
result = linear_search(arr,x)
if result != -1:
    print('Element found at index',result)
else:
    print('Element not found')