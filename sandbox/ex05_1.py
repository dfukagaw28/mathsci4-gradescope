N = int(input())
for n in range(2, N+1):
    is_prime = True
    for m in range(2,n):
        if n % m == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
