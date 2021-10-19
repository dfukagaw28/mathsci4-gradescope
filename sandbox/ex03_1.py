h=int(input())
if 0 <= h <= 11:
    print('おはようございます')
elif h == 12:
    print('お昼です')
elif 13 <= h <= 18:
    print('こんにちは')
elif 19 <= h <= 23:
    print('こんばんは')
else:
    print('範囲外です')
