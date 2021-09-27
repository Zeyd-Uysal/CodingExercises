def valid_solution(board):
    if any(0 in sublist for sublist in board):
        return False
    for i in range(len(board)):
        if len(set(board[i])) != len(board[i]):
            return False
        lst = []
        for j in range(len(board[i])):
            lst.append(board[j][i])
        if len(set(lst)) != len(lst):
            return False
    for i in range(0,len(board),3):
        for j in range(0,len(board),3):
            lst = []
            for k in range(3):
                for l in range(3):
                    lst.append(board[i+l][j+k])

                if len(set(lst)) != len(lst):
                    return False 
    return True