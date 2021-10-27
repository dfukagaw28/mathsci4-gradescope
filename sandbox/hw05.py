s = input()
n = len(s)  # 入力された文字列 s の長さ
goukei = 0  # 合計値を記憶するための変数（0 で初期化しておく）
temp = ''   # 空の文字列
for i in range(0, n + 1):
    if i == n or s[i] == ',':
        goukei += float(temp)
        temp = ''
    else:
        temp += s[i]
print(goukei)
