from typing import List
defaultSudoku=[
    [0, 0, 0, 8, 0, 0, 4, 0, 3],
    [2, 0, 0, 0, 0, 4, 8, 9, 0],
    [0, 9, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 2, 9, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 6, 5, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 6, 2, 7, 0, 0, 0, 0, 1],
    [4, 0, 3, 0, 0, 6, 0, 0, 0]
]
#checks if sudoku board has no more digits to add
def printSudoku(grid:List[List[int]])->None:
    for i in grid:
        print(i)
def sudokuFilled(grid:List[List[int]])->bool:
    for i in grid:
        for j in i:
            if j==0:
                return False
    return True
#returns True if new number is valid under sudoku rules
def checkSudoku(grid:List[List[int]],y:int,x:int,num:int)->bool:
    for i in range(9):
        if grid[y][i]==num or grid[i][x]==num:
            return False#checking row and column
    squarex=x-x%3
    squarey=y-y%3#checking square
    for i in range(3):
        for j in range(3):
            if grid[squarey+i][squarex+j]==num:
                return False
    return True#all tests passed

#solves using recursion and backtracking
def sudokuSolve(grid:List[List[int]])->bool:
    if sudokuFilled(grid):#stop when we have a solution
        return True
    for i in range(9):
        for j in range(9):#iterates all the grid
            if(grid[i][j]==0):
                for k in range(1,10):#all the possible numbers
                    if checkSudoku(grid,i,j,k):
                        grid[i][j]=k
                        #visualize()
                        #print every step with console or
                        #pygame or something
                        if sudokuSolve(grid):
                            return True
                        grid[i][j]=0#backtracking
                return False

def main():
    sudokuSolve(defaultSudoku)
    printSudoku(defaultSudoku)

if __name__=="__main__":
    main()