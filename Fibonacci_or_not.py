n=int(input())
c=0
b=1
a=1
if n==0 and n==1:
    print("True")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("True")
    else:
        print("False")
    