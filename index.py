def search(n):
    ma=max(n)
    m=n[0]
    for i in range(len(n)-1):
        if n[i]>=m and n[i]<ma:
            m=n[i]
    print(m)
        

n=[12,2,3,1,2,3,4,56,6778,323,1]
search(n)

