class Solution:
    """
    The solution has the following complexity:
    Time:  O(n^2)
    Space: O(n^2)

    We have 3 lists of hashsets that contain the elements from each line, each column and each box.
    The we iterate through each element of the matrix and check if the element already exist on the line, column or box.
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        lines   = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        boxes   = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":

                    if board[i][j] not in lines[i]:
                        lines[i].add(board[i][j])
                    else:
                        return False

                    if board[i][j] not in columns[j]:
                        columns[j].add(board[i][j])
                    else:
                        return False

                    index = (int(i/3) * 3) + int(j/3)
                    if board[i][j] not in boxes[index]:
                        boxes[index].add(board[i][j])
                    else:
                        return False

        return True

