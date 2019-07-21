def binarySearch(arr,low,high,key):
    while low<=high:
        mid=low+(high-1)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low=mid+1
        else:
            high=mid-1
    else:return -1

arr=[10,20,30,40,70]
key=20
res=binarySearch(arr,0,len(arr)-1,key)
if res==-1:
    print('not found')
else:print('found at position',res)