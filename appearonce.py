def mid(arr,low,high):
    if low==high:
        return arr[low]

    mid=(high-low)//2
    if mid%2==0:

        if arr[mid]==arr[mid+1]:
            return mid(arr,mid+2,high)
        else:
            return mid(arr,low,mid)
    else:
        if arr[mid]==arr[mid-1]:
            return mid(arr,mid+1,high)
        else:
            return mid(arr,low,mid-1)


    

arr=[11,22,33,66,4,77,88]
result=mid(arr,0,len(arr)-1)
if result is not None:
    print("hello world",result)

else:
    print("hello you")
