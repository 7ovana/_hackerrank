# Matrix Layer Rotation
# 
# difficulty: hard
# maximum points: 80

def pm(matrix:list, m:int, n:int):
    """ Print a given m*n matrix.
    """

    if type(matrix[0]) == int:
        for i in range(m):
            print (matrix[i*n : i*n + n])
    else:
        print('\n'.join([''.join([("{:"+str(m)+"}").format(item) for item in row]) for row in matrix]))

def flatten_outline(matrix:list, m:int, n:int) -> list:
    """ Flatten the outline for a given m*n matrix.
    """

    first_row = matrix[0]
    last_row = matrix[-1]
    left_border = [matrix[i][0] for i in range(m)]
    right_border = [matrix[i][-1] for i in range(m)]

    return first_row[:-1] + right_border[:-1] + last_row[1:][::-1] + left_border[::-1][:-1]

def get_all_outlines(matrix:list, m:int, n:int) -> list:
    """ Return all outlines of a m*n matrix.
    """

    outlines = dict()
    _m,_n = m,n
    start = 0
    submatrix = matrix

    while 1:
        outlines.update({(_m,_n) : flatten_outline(submatrix,_m,_n)})
        start += 1
        _m -= 2
        _n -= 2
        submatrix = [submatrix[i][1:-1] for i in range(1,_m+1)]
        if _m == 0 or _n == 0:
            break

    return outlines

def reconstruct_matrix(outlines:dict, m:int, n:int) -> list:
    """ Reconstruct matrix from its outlines.
    """
    
    start = 0
    matrix = [[0]*n]*m

    for b in outlines:

        _m = b[0]
        _n = b[1]

        submatrix = [[0]*_n]*_m
    
        arr = outlines[b]

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

def matrixRotation(matrix, r):
    """ Rotate the matrix.
    """

    m = len(matrix)
    n = len(matrix[0])

    outlines = get_all_outlines(matrix,m,n)

    for b in outlines:
        _m = b[0]
        _n = b[1]
        size = 2*((_m+_n)-2)
        outlines[b] = outlines[b][r%size:] + outlines[b][:r%size]

    rm = reconstruct_matrix(outlines,m,n)

    [print(*rm[i]) for i in range(m)]


if __name__ == '__main__':

    m = 4
    n = 4
    r = 2

    matrix = [[1,2,3,4], [7,8,9,10], [13,14,15,16], [19,20,21,22], [25,26,27,28]]
    matrixRotation(matrix,1)
