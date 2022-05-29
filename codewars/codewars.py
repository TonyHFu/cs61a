def determinant(matrix):
    
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        sign = 1
        det = 0
        for i in range(len(matrix)):
            submatrix = []
            for j in range(1, len(matrix)):
                submatrix += [[matrix[j][k] for k in range(len(matrix)) if k != i]]
            det += sign * matrix[0][i] * determinant(submatrix)
            sign *= -1
        return det

i = 0

matrix = [[2,4,2],[3,1,1],[1,2,0]]
def get_submatrix(matrix, i):
    submatrix = []
    for j in range(1, len(matrix)):
        submatrix += [[matrix[j][k] for k in range(len(matrix)) if k != i]]
    return submatrix


def smallest_factor(n):
    if n == 1:
        return 1

    i = 2
    while n % i != 0:
        i += 1
    return i

        
    
def prime_factors(n):   
    leaves = {}
    
    while n != 1:
        factor = smallest_factor(n)
        if factor in leaves:
            leaves[factor] += 1
        else:
            leaves[factor] = 1
        n /= factor
    print(n)
    print(leaves)
    

    
        
    
    
            
                
    