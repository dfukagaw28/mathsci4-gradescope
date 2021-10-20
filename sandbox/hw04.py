ans = 0

for k in range(10):
    x = int(input())
    if x % 2 == 1:
        ans = max(ans, x)

if ans > 0:
    print('最も大きい奇数は', ans, 'です。')

else:
    print('奇数がありません。')
