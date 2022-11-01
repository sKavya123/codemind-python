def f(n):
    sum_n=sum(map(int,str(n)))
    if sum_n>9:
        return f(sum_n)
    return sum_n
n=int(input())
print(f(n))