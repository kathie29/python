def fib (x):
    if x==1:
        return 1
    else:
        return x*fib(x-1)
k = input("please enter a number")

print(fib(int(k)))
