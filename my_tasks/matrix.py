# возведение матрицы в степень

n = int(input())  

res = [input().split() for _ in range(n)]
for a in range(n):
    for b in range(n):
        res[a][b] = int(res[a][b])
res2 = []
for a1 in range(n):
    temp = []
    for b1 in range(n):
        temp.append(res[a1][b1])
    res2.append(temp)
        
degree = int(input())  # ввод степени

res_end = []
for c in range(n):
    temp = []
    for d in range(n):
        temp.append(0)
    res_end.append(temp)
    
for el in range(degree-1):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res_end[i][j] += int(res[i][k]) * int(res2[k][j])
    res = res_end
    res_end = []
    for el2 in range(n):
        temp = []
        for el3 in range(n):
            temp.append(0)
        res_end.append(temp)
    
for aa in range(n):
    for bb in range(n):
        print(res[aa][bb], end=' ')
    print()