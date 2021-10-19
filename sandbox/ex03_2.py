y=int(input())
if y % 400 == 0:
    print('Yes')
elif y % 100 == 0:
    print('No')
elif y % 4 == 0:
    print('Yes')
else:
    print('No')
