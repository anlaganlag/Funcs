class Solution:
    def numRookCaptures(self, g: List[List[str]]) -> int:
        """最厲害的是方位數組,就是靠i去遍歷讀出,讀出4個方向
	  的坐標..

	"""
        y,x,cnt = 0,0,0
        dy = [-1 , 1 , 0 , 0]
        dx = [0 , 0 , 1 , -1]
        for i in range(8):
            for j in range(8):
                if g[i][j] == 'R':
                    y,x = i,j
        for i in range(4):
            off_set = 1
            while True:
                y_ = y + off_set*dy[i]
                x_ = x + off_set*dx[i]
                if y_<0 or y_>7 or x_<0 or x_>7:
                    break
                else:
                    if g[y_][x_] =='B':
                        break 
                    if g[y_][x_] == 'p':
                        cnt +=1
                        break
                off_set +=1
        return cnt


        

"""
999. Available Captures for Rook

On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""
