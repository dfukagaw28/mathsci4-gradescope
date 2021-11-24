def sum_digits(s):
    if type(s) != str:
        raise TypeError(f'文字列でない引数が渡されました: {s}')
    x = 0
    flag = False
    for i in range(len(s)):
        if s[i].isdigit():
            x += int(s[i])
            flag = True
    if not flag:
        raise ValueError(f'文字列に数字が含まれていません: {s}')
    return x

if __name__ == '__main__':
    #sum_digits(123)
    #sum_digits('hello')
    print(sum_digits('12345'))
