class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        l = len(board)
        t = 0
        index = []
        for i in board:
            if 'R' in i:
                L = board.index(i)
                n = i.index('R')
                break
        for i in range(l):
            index.append(board[i][n])
        column = list(board[L])

        index = ''.join(index)
        column = ''.join(column)
        index = index.replace('.','')
        column = column.replace('.','')
        for i in range(len(index)):
            if index == 'R':
                break
            if index[i] == 'R':
                if index[i-1] == 'p':
                    if i != 0:
                        t+=1
                if i != len(index)-1:
                    if index[i+1] == 'p':
                        t+=1
        for i in range(len(column)):
            if column == 'R':
                break
            if column[i] == 'R':
                if column[i-1] == 'p':
                    if i != 0:
                        t+=1
                if i != len(column)-1:
                    if column[i+1] == 'p':
                        t+=1
        return t


s= Solution()
print(s.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))