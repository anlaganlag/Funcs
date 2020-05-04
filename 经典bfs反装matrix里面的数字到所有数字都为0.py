from copy import deepcopy
def minFlips(mat):
    row, col = len(mat), len(mat[0])
    size = row * col # The size of matrix
    def revert(i, j, matrix): # Revert the position
        if i < 0 or i >= row or j < 0 or j >= col:
            return 
        matrix[i][j] = 1 - matrix[i][j]        
    def matrix_bits(matrix):
        res = ''
        for i in range(size):
            res += str(matrix[i // col][i % col])
        return res         
    q, visited= [mat], [matrix_bits(mat)]
    forward = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]#保证本点和周围4个点都发生反转..
    res = 0
    while q:
        n = len(q)
        for _ in range(n):
            tmp = q.pop(0)
            if not sum(sum(tmp,[])):
                return res
            for i in range(size):
                tmp_cp = deepcopy(tmp)
                r , c = i // col , i % col
                for f in forward:
                    revert(r+f[0],c+f[1],tmp_cp)
                bits = matrix_bits(tmp_cp)
                if bits in visited:
                    continue
                        visited.append(bits)
                        q.append(tmp_cp)
                res +=1
            return -1
        
