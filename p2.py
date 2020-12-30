fib = [1, 2]
i = 0
n = 0
while n < 4000000:
    n = fib[i] + fib[i+1]
    fib.append(n)
    i += 1

print(sum(map(lambda i: i if i % 2 == 0 else 0,fib)))
