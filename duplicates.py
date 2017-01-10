def median(x):
    for n in len(x):
        if x[n]>x[n+1]:
            temp=x[n]
            x[n]=x[n+1]
            x[n+1]=temp
    return x

median([2,4,5,3,6])