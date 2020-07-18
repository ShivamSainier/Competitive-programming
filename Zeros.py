def count(n):
    j=0
    for i in n:
        if i==1:
            continue
        else:
            j=j+1
    return j


n=[1,1,1,1,0,0,0,0,0,0]
result=count(n)
print(result)
