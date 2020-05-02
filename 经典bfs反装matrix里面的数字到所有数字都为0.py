class Solution:
        from copy import deepcopy
        def minFlips(self, mat: List[List[int]]) -> int:
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
                queue_length = len(q)
                for _ in range(queue_length):
                    tmp = q.pop(0)
                    if sum(sum(tmp, [])) == 0:
                        return res                  
                    for i in range(size):
                        tmp_copy = deepcopy(tmp)
                        r, c = i // col, i % col
                        for f in forward:
                            revert(r + f[0], c + f[1], tmp_copy)
                        bits = matrix_bits(tmp_copy)
                        if bits in visited: 
                            continue
                        visited.append(bits)
                        q.append(tmp_copy)
                res += 1
            return -1
        

