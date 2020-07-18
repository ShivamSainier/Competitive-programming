def root(x):
    i=1
    result=1
    while result<=x:
        i=i+1
        result=i*i
    return i-1


x=11
print(root(x))
