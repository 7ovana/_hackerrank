from itertools import chain

def pm(matrix,m,n):
    if type(matrix[0]) == int:
        for i in range(m):
            print (matrix[i*n : i*n + n])
    else:
        print('\n'.join([''.join([("{:"+str(m)+"}").format(item) for item in row]) for row in matrix]))

def cycle(m,n):
    r = 0
    l = []
    while m>=2 and n>=2:
        l.append(2*((m+n)-2))
        m-=2
        n-=2
    return l

def flatten_border(matrix : list) -> list:
    result = matrix[0]
    return 


m = 4
n = 4
r = 2
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#matrix_2 = [[1,2,3,4], [7,8,9,10], [13,14,15,16], [19,20,21,22], [25,26,27,28]]
mflat = [matrix[i][j] for i in range(m) for j in range(n)]
initial_indices = list(range(n*m))
pm(matrix,m,n)

flatten_border(matrix) # flatten border in anticlockwise order