def occur(n,x):
    r=0
    for i in n:
        if i==x:
            r=r+1
    return r
        

n=[11,34,223,67,34,11,11,67,78,7,67,67,67]
x=11
result=occur(n,x)
print(result)
