def element(x,y):
    r=0
    for  i in range(0,len(x)-1):
        if x[i]==y[i]:
            continue
        else:
            r=r+i
        return r+1




x=[12,23,5,34,45,67,78]
y=[12,23,34,45,67,78]
result=element(x,y)
print(result)
