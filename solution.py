puzzle = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

#print puzzle in console
def print_puzzle(puzzle):
    print()
    for i in range(len(puzzle)):
        if i%3 == 0 and i!=0:
            print("------------------------")
        for j in range(len(puzzle[i])):
            if j%3 == 0 and j!=0:
                print(" | ", end="")
            if j%8 == 0 and j!=0:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end="")
"""
Order of Execution:
    - Find empty position
    - test an input for validity starting from 1
    - check if that input already exists in that row
    - check if that input already exists in that column
    - check if it already exists in given 3x3 box
    - if not assign that input to the empty position
    - if it already exists try it's succesor
    - if there's no more available successor then we take a 
      step back to the previous cell and try the next following value
    - repeat this process until solved
"""
def search_for_zero(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j]==0:
                return i,j
    return None

def solve(puzzle):
    cell = search_for_zero(puzzle)
    if not cell:
        return True
    else:
        row, col = cell
    for i in range(1,10):
        if is_valid(puzzle, row, col, i):
            puzzle[row][col] = i
            if solve(puzzle):
                print_puzzle(puzzle)
                return True
            puzzle[row][col]=0
    return False


def is_valid(puzzle, row, col, n):
    for i in range(9):
        if puzzle[row][i]==n or puzzle[i][col]==n:
            return False
    for i in range(3):
        for j in range(3):
            if(puzzle[i + row-row%3][j + col-col%3] == n):
                return False
            else:
                return True
solve(puzzle)