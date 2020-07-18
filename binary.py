def search(lis,n):
    lb=0
    ub=len(lis)-1
    while lb<=ub:
        mid=lb+ub//2
        if lis[mid]==n:
            return True
        else:
            if lis[mid]<n:
                lb=mid+1
            else:
                ub=mid-1
    return False
    


lis=[2,3,4,12,23,34,123]
n=3
if search(lis,n):
    print("Found")

else:
    print("Not Found")
