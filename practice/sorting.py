def sorting(num):
    l=[]
    a=num[0]
    for i in num:
        if i>a:
            l.insert(0,i)
        else:
            l.append(i)
    return l

print(sorting([1,2,3,4,5,6]))

def mymax(num):
    n=num[0]
    for i in num:
        if n<i:
            n=i
    return n

print(mymax([2,1,30,4,2,5,3,9]))

def mymax(num):
    n=num[0]
    for i in num:
        if n>i:
            n=i
    return n

print(mymax([2,1,30,4,0,2,5,3,9]))