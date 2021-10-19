x = int(input())
y = int(input())
z = int(input())
ans = 0
if x % 2 == 1:
    ans = max(ans, x)
if y % 2 == 1:
    ans = max(ans, y)
if z % 2 == 1:
    ans = max(ans, z)
if ans > 0:
    print('最も大きい奇数は', ans, 'です。')
else:
    print('奇数がありません。')
