def buildings(sun):
    j=1
    k=sun[0]
    for i in range(0,len(sun)):
        if sun[i]>k:
            k=sun[i]
            j=j+1
    return j
        



n=[7,4,8,2,9]
result=buildings(n)
print(result)
