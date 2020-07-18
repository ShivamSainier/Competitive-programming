def transition(n):
    m=len(n)-1
    for i in range(0,len(n)-1):
        if n[i]>m:
            m=n[i]
        else:
            continue
    return m


n=[12,1,2,3,45,13,2,456]
j=transition(n)
print(j)
