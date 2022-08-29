
N = 9

def isSafe(su, row, col, num):
    for i in range(9):
        if (su[row][i] == num or su[i][col] == num):
            return False
        
        startR = row - row % 3
        startC = col - col % 3

        for i in range(3):
            for j in range(3):
                if (su[startR + i][startC + j] == num):
                    return False
    return True

def solve(sud, row, col):
    if row == N -1 and col == N:
        return True
    if col == N:
        row += 1
        col = 0
    if sud[row][col] > 0:
        return solve(sud, row, col+1)

    for num in range(1,N+1):
        if isSafe(sud, row, col, num):
            sud[row][col] = num
            
            if solve(sud, row, col+1):
                return True
        
        sud[row][col] = 0
    return False



def solver(sudo):
    if solve(sudo,0,0):
        return sudo
    else:
        return "NO"
