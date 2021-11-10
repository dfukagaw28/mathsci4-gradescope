def findCubicRoot(x, epsilon):
    # 探索範囲の下限（low）と上限（high）を定める
    # つねに low ** 3 < x ≦ high ** 3 が成り立つ
    if x < -1:
        low, high = x, -1
    elif x < 0:
        low, high = -1, x
    elif x < 1:
        low, high = x, 1
    else:
        low, high = 1, x

    while True:
        # 次の推定値を計算する
        # low < ans < high が成り立つ
        ans = (high + low) / 2.0

        # 現在の状態を表示する
        #print('low =', low, 'high =', high, 'ans =', ans)

        # もし推定値の 3 乗と入力 x の誤差が許容範囲内なら繰り返しを終える
        if abs(ans ** 3 - x) < epsilon:
            break

        # 探索範囲を更新する
        if ans ** 3 < x:
            low = ans
        else:
            high = ans

    return ans

x = float(input())
eps = float(input())
ans = findCubicRoot(x, eps)
print(ans)
