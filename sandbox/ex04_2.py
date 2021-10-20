n = int(input())
count = 0
for m in range(1, n + 1):
    if n % m == 0:
        count += 1
print(count)
