# TO DO:  FIX GET ALL BORDERS

def pm(matrix,m,n):
    if type(matrix[0]) == int:
        for i in range(m):
            print (matrix[i*n : i*n + n])
    else:
        print('\n'.join([''.join([("{:"+str(m)+"}").format(item) for item in row]) for row in matrix]))

def flatten_border(matrix:list, m:int, n:int) -> list:

    first_row = matrix[0]
    last_row = matrix[-1]
    left_border = [matrix[i][0] for i in range(m)]
    right_border = [matrix[i][-1] for i in range(m)]

    return first_row[:-1] + right_border[:-1] + last_row[1:][::-1] + left_border[::-1][:-1]

def reconstruct_rotated_matrix(borders, m, n):
    # assuming the borders are already rotated r times
    
    start = 0
    matrix = [[0]*n]*m

    for b in borders:

        _m = b[0]
        _n = b[1]

        submatrix = [[0]*_n]*_m
    
        arr = borders[b]

        first_row = arr[:_n]
        arr = arr[_n-1:]
        right_border = arr[:_m]
        arr = arr[_m-1:]
        last_row = arr[:_n][::-1]
        arr = arr[_n-1:]
        left_border = [first_row[0]] + arr[::-1]

        submatrix[0] = first_row
        submatrix[-1] = last_row

        for i in range(1,_m-1):
            submatrix[i] = [left_border[i]] + [0]*(_n-2) + [right_border[i]]
        
        if _m == m and _n == n:
            matrix[:] = submatrix[:]
        else:    
            for i in range(start,m-start):
                for j in range(start,n-start):
                    matrix[i][j] =  submatrix[i-start][j-start]
                
        start += 1

    return matrix
 
 
def get_all_borders(matrix:list, m:int, n:int) -> list:

    borders = dict()
    _m,_n = m,n
    start = 0
    submatrix = matrix
    while 1:
        borders.update({(_m,_n) : flatten_border(submatrix,_m,_n)})
        start += 1
        _m -= 2
        _n -= 2
        submatrix = [submatrix[i][1:-1] for i in range(start,_m+1)]
        if _m == 0 or _n == 0:
            break
    return borders

def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    borders = get_all_borders(matrix,m,n)
    for b in borders:
        borders[b] = borders[b][r:] + borders[b][:r]
    return reconstruct_rotated_matrix(borders,m,n)

m = 4
n = 4
r = 2
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix_2 = [[1,2,3,4], [7,8,9,10], [13,14,15,16], [19,20,21,22], [25,26,27,28]]


print(matrixRotation(matrix,1))

