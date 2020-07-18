def search(li,n):
    for i in li:
        if i==n:
            return True
    return False

li=[4,5,6,21,3,4,5,6]
n=6
if search(li,n):
    print("Found")
else:
    print("Not Found")
