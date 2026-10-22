class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict, colDict, spaceDict = defaultdict(set), defaultdict(set), defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[c][r] == ".":
                    continue
                
                if board[c][r] in rowDict[r] or board[c][r] in colDict[c] or board[c][r] in spaceDict[(c//3, r//3)]:
                    return False

                rowDict[r].add(board[c][r])
                colDict[c].add(board[c][r])
                spaceDict[((c//3, r//3))].add(board[c][r])
        
        return True
                






        