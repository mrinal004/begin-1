def linearSearch(arr,key):
    n=len(arr)
    for i in range(0,n):
        if arr[i]==key:
            return i
    else:
        return -1

arr=[10,2,34,41,56]
key=56
res=linearSearch(arr,key)
if res==-1:
    print("element not found")
else:
    print("element found at index: %d"%res)
