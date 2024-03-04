from random import randint

def CreateGrid(columns, rows):
    matrix = []
    
    for i in range(rows):
        row = []

        for j in range(columns):
            space = 0
            row.append(space)
    
        matrix.append(row)
    return matrix

def InsertFirstGen(matrix, population, columns, rows):
    i = 0
    while i < population:
        row = randint(0, rows-1)
        column = randint(0, columns-1)
        if matrix[row][column] == 0:
             matrix[row][column] = 1
             i = i + 1
    return matrix

def NeighboursCheck(matrix, columns, rows, column, row):
    neighbours = 0

    if row == 0 and column == 0:
        for x in range(0, 2):
            for y in range(0, 2):
                if matrix[row+x][column+y] == 1:
                    neighbours = neighbours+1
                if x == 0 and y == 0 and matrix[row][column] == 1:
                    neighbours = neighbours-1
    elif row == 0 and column == columns-1:
        for x in range(0, 2):
            for y in range(-1, 1):
                if matrix[row+x][column+y] == 1:
                    neighbours = neighbours+1
                if x == 0 and y == 0 and matrix[row][column] == 1:
                    neighbours = neighbours-1
    elif row == rows-1 and column == 0:
        for x in range(-1, 1):
            for y in range(0, 2):
                if matrix[row+x][column+y] == 1:
                    neighbours = neighbours+1
                if x == 0 and y == 0 and matrix[row][column] == 1:
                    neighbours = neighbours-1
    elif row == rows-1 and column == columns-1:
        for x in range(-1, 1):
            for y in range(-1, 1):
                if matrix[row+x][column+y] == 1:
                    neighbours = neighbours+1
                if x == 0 and y == 0 and matrix[row][column] == 1:
                    neighbours = neighbours-1
    elif row == 0:
        for x in range(0, 2):
            for y in range(-1, 2):
                if matrix[row+x][column+y] == 1:
                    neighbours = neighbours+1
                if x == 0 and y == 0 and matrix[row][column] == 1:
                    neighbours = neighbours-1
    elif row == rows-1:
        for x in range(-1, 1):
            for y in range(-1, 2):
                if matrix[row+x][column+y] == 1:
                    neighbours = neighbours+1
                if x == 0 and y == 0 and matrix[row][column] == 1:
                    neighbours = neighbours-1
    elif column == 0:
        for x in range(-1, 2):
            for y in range(0, 2):
                if matrix[row+x][column+y] == 1:
                    neighbours = neighbours+1
                if x == 0 and y == 0 and matrix[row][column] == 1:
                    neighbours = neighbours-1
    elif column == columns-1:
        for x in range(-1, 2):
            for y in range(-1, 1):
                if matrix[row+x][column+y] == 1:
                    neighbours = neighbours+1
                if x == 0 and y == 0 and matrix[row][column] == 1:
                    neighbours = neighbours-1
    else:
        for x in range(-1, 2):
            for y in range(-1, 2):
                if matrix[row+x][column+y] == 1:
                    neighbours = neighbours+1
                if x == 0 and y == 0 and matrix[row][column] == 1:
                    neighbours = neighbours-1

        
    return neighbours

def NextGen(matrix, columns, rows):
    newMatrix = matrix
    for i in range(rows):
        for j in range(columns):
            cellNeighbours = NeighboursCheck(matrix, columns, rows, j, i)
            #print(cellNeighbours)
            if matrix[i][j] == 0:
                if cellNeighbours == 3:
                    newMatrix[i][j] == 1

            if matrix[i][j] == 1:
                if cellNeighbours < 2 or cellNeighbours > 3:
                    newMatrix[i][j] == 0
    return newMatrix
            

Columns = int(input("Enter the number of columns: "))
Rows = int(input("Enter the number of rows: "))
Population = int(input("Enter the population number: "))
Gens = int(input("Enter the number of generations you wish to follow: "))

while Population > (Columns*Rows):
    Population = int(input("Population too big, enter a smaller population number: "))

Grid = CreateGrid(Columns, Rows)

Game = InsertFirstGen(Grid, Population, Columns, Rows)

for number in range(Gens):
    newGame = NextGen(Game, Columns, Rows)
    print("Generation " + str(number+1) + ": ")
    for i in newGame:
        print(i)

#print matrix
'''for row in Game:
    print(row)'''