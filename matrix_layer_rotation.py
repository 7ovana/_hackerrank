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

def flatten_border(matrix:list, m:int, n:int) -> list:

    first_row = matrix[0]
    last_row = matrix[-1]
    left_border = [matrix[i][0] for i in range(m)]
    right_border = [matrix[i][-1] for i in range(m)]

    return first_row[:-1] + right_border[:-1] + last_row[1:][::-1] + left_border[::-1][:-1]

def reconstruct_rotated_matrix(borders, m, n):
    # assuming the borders are already rotated r times
    #for border in borders:
        # we should put this border where it belongs on the original matrix
        # matrix[0] = first row
        # [matrix[i][0] for i in range(m)] = right border
        # matrix[-1] = last row
        # [matrix[i][-1] for i in range(m)] = left border
    return 
 
 
def get_all_borders(matrix:list, m:int, n:int) -> list:

    borders = []
    _m,_n = m,n
    start = 0
    submatrix = matrix
    while 1:
        print(submatrix)
        print(f"m = {_m} n = {_n}")
        borders.append(flatten_border(submatrix,_m,_n))
        start += 1
        _m -= 2
        _n -= 2
        submatrix = [submatrix[i][1:-1] for i in range(start,_m+1)]
        if _m == 0 or _n == 0:
            break
    return borders

m = 4
n = 4
r = 2
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix_2 = [[1,2,3,4], [7,8,9,10], [13,14,15,16], [19,20,21,22], [25,26,27,28]]
mflat = [matrix[i][j] for i in range(m) for j in range(n)]
initial_indices = list(range(n*m))
pm(matrix,m,n)

#print(flatten_border(matrix,m,n)) # -> [1,2,3,4,8,12,16,]
print(get_all_borders(matrix_2,5,4))
