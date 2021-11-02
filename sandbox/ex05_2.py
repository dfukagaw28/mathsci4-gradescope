S = input() + ','
L = len(S)
temp = ''
for i in range(L):
    if S[i] == ',':
        print(temp)
        temp = ''
    else:
        temp += S[i]
