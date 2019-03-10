def chop(l):
    l[:]=l[1:]
    del(l[-1])
    return None

def middle(l):
    n=len(l)
    new=l[1:n-1]
    return new

mylist1 = [1,2,3,4]
mylist2 = [1,2,3,4]

c=chop(mylist1)
print(mylist1)
print(c)

m=middle(mylist2)
print(mylist2)
print(m)