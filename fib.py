numberlist = []
i = 0
for i in range(20):
    numberlist.append(i)

print numberlist

fibonaccinumbers = []

for n in numberlist:
    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    a = fib(n)
    fibonaccinumbers.append(a)


print a
