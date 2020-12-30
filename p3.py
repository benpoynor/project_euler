n = 600851475143

def split(n:int):
    for i in range(2, int(n**(1/2.0)), 1):
        if (n/i) % 1 == 0:
            return i, int(n/i)
    return n, 1

def primes(n:int) -> list:
    def factor(a: list):
        for i in a:
            s = split(i)
            if 1 not in s:
                a.remove(i)
                a.extend(s)
                factor(a)
        return a
    return factor([n])

print(max(primes(n)))
