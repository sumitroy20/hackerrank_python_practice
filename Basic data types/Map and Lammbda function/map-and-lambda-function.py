def fibonacci(n):
    # return a list of fibonacci numbers
    num_list=list()
    if n==0:
        return []
    else:
        num_list.append(0)
    c=1
    b=0
    for i in range(n-1):
        num_list.append(c)
        a=b
        b=c
        c=a+b
    return num_list

cube = lambda x:pow(x,3)

n = int(input())
print(list(map(cube, fibonacci(n))))