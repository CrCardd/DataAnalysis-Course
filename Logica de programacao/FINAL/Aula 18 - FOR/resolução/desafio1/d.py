def iterate(matriz):
    indices_valores = []
    l = -1
    c = -1
    for i in range(int(len(matriz)/2), 0, -2):

        for _ in range(i):
            l+=1
            c+=1
            indices_valores.append(
                (
                    (matriz[l][c], matriz[c][l]),                                                               # 1 quadr
                    (matriz[l][len(matriz)-1-c], matriz[c][len(matriz)-1-l]),                                   # 2 quadr
                    (matriz[len(matriz)-1-l][c], matriz[len(matriz)-1-c][l]),                                   # 3 quadr
                    (matriz[len(matriz)-1-l][len(matriz)-1-c], matriz[len(matriz)-1-c][len(matriz)-1-l])        # 4 quadr
                )
            )
        
        c-=1

        for _ in range(i-1):
            indices_valores.append(
                (
                    (matriz[l][c], matriz[c][l]),                                                               # 1 quadr
                    (matriz[l][len(matriz)-1-c], matriz[c][len(matriz)-1-l]),                                   # 2 quadr
                    (matriz[len(matriz)-1-l][c], matriz[len(matriz)-1-c][l]),                                   # 3 quadr
                    (matriz[len(matriz)-1-l][len(matriz)-1-c], matriz[len(matriz)-1-c][len(matriz)-1-l])        # 4 quadr
                )
            )
            
            l-=1
            c-=1

        l+=1
    return indices_valores



develop = [
    [6,  73, 29, 12, 32,   100, 39, 18, 67, 85],
    [70, 20, 59, 4,  28,   43,  3,  60, 93, 84],
    [95, 40, 2,  99, 33,   52,  47, 21, 30, 23],
    [17, 71, 35, 10, 61,   91,  92, 42, 98, 13],
    [57, 26, 22, 7,  14,   11,  55, 25, 41, 76],
                           
    [27, 16, 45, 63, 15,   50,  72, 66, 31, 65],
    [89, 75, 48, 94, 1,    19,  80, 53, 36, 58],
    [24, 83, 34, 62, 78,   5,   9,  97, 82, 96],
    [38, 88, 8,  68, 74,   79,  46, 37, 64, 49],
    [87, 90, 44, 51, 86,   77,  56, 69, 81, 54]
]

test_result = [
    [1,  9,  10, 14, 15,   15, 14, 10, 9,  1 ],
    [9,  2,  8, 11,  13,   13, 11, 8,  2,  9 ],
    [10, 8,  3,  7,  12,   12, 7,  3,  8,  10],
    [14, 11, 7,  4,  6,    6,  4,  7,  11, 14],
    [15, 13, 12, 6,  5,    5,  6,  12, 13, 15],
                            
    [15, 13, 12, 6,  5,    5,  6,  12, 13, 15],
    [14, 11, 7,  4,  6,    6,  4,  7,  11, 14],
    [10, 8,  3,  7,  12,   12, 7,  3,  8,  10],
    [9,  2,  8,  11, 13,   13, 11, 8,  2,  9 ],
    [1,  9,  10, 14, 15,   15, 14, 10, 9,  1 ]
]


result = iterate(test_result)
print(result)