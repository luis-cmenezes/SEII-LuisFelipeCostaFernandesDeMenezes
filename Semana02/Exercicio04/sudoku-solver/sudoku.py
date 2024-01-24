def find_next_empty_space(puzzle):

    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column

    return None, None

def is_valid(puzzle, guess, row, column):
    #check de linha
    if guess in puzzle[row]:
        return False
    
    #check de coluna
    column_vals = [puzzle[i][column] for i in range(9)]
    if guess in column_vals:
        return False
    
    #check de chunk
    chunk_row = row//3 * 3
    chunk_column = column//3 * 3
    for r in range(chunk_row, chunk_row+3):
        for c in range(chunk_column, chunk_column+3):
            if puzzle[r][c] == guess:
                return False
        
    return True

def solver(puzzle):

    r, c = find_next_empty_space(puzzle)

    if r is None:
        return True
    
    for guess in range(1, 10):

        if is_valid(puzzle, guess, r, c):
            puzzle[r][c] = guess
        
            if solver(puzzle):
                return True
        
        puzzle[r][c] = -1
    
    return False

if __name__ == '__main__':
    board = [
        [-1, -1,  4,    -1, -1,  7,      3, -1, -1],
        [-1, -1,  9,     8, -1, -1,     -1, -1, -1],
        [ 3,  8, -1,    -1,  1, -1,     -1,  2, -1],

        [-1, -1, -1,    -1, -1,  6,     -1,  1, -1],
        [-1, -1,  3,    -1, -1, -1,     -1, -1, -1],
        [ 7,  5, -1,     4, -1, -1,      2, -1, -1],

        [-1, -1, -1,    -1,  4, -1,     -1, -1,  5],
        [-1,  9, -1,    -1, -1, -1,     -1, -1, -1],
        [ 8,  2, -1,     5, -1, -1,      7, -1, -1],
    ]

    print(solver(board))
    print(board)