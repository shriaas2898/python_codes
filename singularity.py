"""'''author: shriaas2898
   description: Python file contains function to calculate determinant of matrix
   and a  function to check if the matrix is singular'''
# for calculating determinant of a matrix


def determinant(matrix):

        if 1 == len(matrix):
            return matrix[0][0]

        if 2 == len(matrix):
            return (matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])

        det = 0
        for i in range(len(matrix)):
            minor = matrix[1:]
            minor = list(map(lambda lst :lst[:i] + lst[i+1:],minor ))
            det+= (-1)**i*matrix[0][i]*determinant(minor)
        else:
            return det


def singularity_check(matrix):

    # for checking if matrix is a square matrix
    if len(matrix) != len(matrix[0]):
        NonSquareMatrixExecption = Exception("Supplied matrix is not a square matrix")
        raise NonSquareMatrixExecption

        return False

    if 0 == determinant(matrix):
        return True
    else:
        return False


def build_matrix(file_name):
    file = open(file_name,"r")
    row,column = file.readline().split(",")
    if row != column:
        NonSquareMatrixExecption = Exception("Supplied matrix is not a square matrix")
        raise NonSquareMatrixExecption
    else:
        matrix = []
        for index in range(0,int(row)):
            matrix.append(file.readline().split(","))

        return matrix
if __name__ == '__main__':
    """

''' Modified Code'''
global N 
N = 3
  
# Function to get cofactor of mat[p][q] in temp[][]. 
# n is current dimension of mat[][] 
def getCofactor(mat,temp,p,q,n): 
    i = 0
    j = 0
      
    # Looping for each element of the matrix 
    for row in range(n): 
        for col in range(n): 
              
            # Copying into temporary matrix only  
            # those element which are not in given  
            # row and column 
            if (row != p and col != q): 
                temp[i][j] = mat[row][col] 
                j += 1
                  
                # Row is filled, so increase row 
                # index and reset col index 
                if (j == n - 1): 
                    j = 0
                    i += 1
  
# Recursive function to check if mat[][] is 
# singular or not. */ 
def isSingular(mat,n): 
    D = 0 # Initialize result 
      
    # Base case : if matrix contains single element 
    if (n == 1): 
        return mat[0][0] 
          
    temp = [[0 for i in range(N + 1)] for i in range(N + 1)]# To store cofactors 
      
    sign = 1 # To store sign multiplier 
  
    # Iterate for each element of first row 
    for f in range(n): 
          
        # Getting Cofactor of mat[0][f] 
        getCofactor(mat, temp, 0, f, n) 
        D += sign * mat[0][f] * isSingular(temp, n - 1) 
          
        # terms are to be added with alternate sign 
        sign = -sign 
    return D 
  
# Driver program to test above functions 
if __name__ == '__main__': 
    mat = [[4, 10, 1],[0, 0, 0],[1, 4, -3]] 
    if (isSingular(mat, N)): 
        print("Matrix is Singular") 
    else: 
        print("Matrix is non-singular")     