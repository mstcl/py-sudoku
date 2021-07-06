################
### PACKAGES ###
################

import time

###############
### METHODS ###
###############

def removeZeros():
    global board
    for row in range(9):
        for col in range(9):
            if isinstance(board[row][col], list):
                removeZeros = board[row][col]
                removeZeros = [i for i in removeZeros if i != 0]
                board[row][col] = removeZeros

def form_board(sudoku_string):
    global sudoku
    for i in range(0, len(sudoku_string), 9):
        row = sudoku_string[i:i+9]
        temp = []
        for block in row:
            temp.append(int(block))
        sudoku.append(temp)              

def update():
    global board
    for row in range(9):
        for col in range(9):
            if isinstance(board[row][col], list) and len(board[row][col]) == 1:
                board[row][col] = board[row][col][0]

def display(board):
    for i in board:
        print(i)

def verify(board,row,col,digit):
    for i in range(9):
        if i != col:
            if board[row][i] == digit:
                return False
    for j in range(9):
        if j != row:
            if board[j][col] == digit:
                return False
    box_row = (row//3)*3
    box_col = (col//3)*3
    for i in range(3):
        for j in range(3):
            if box_row+i != row and box_col+j != col and board[box_row+i][box_col+j] == digit:
                return False    
    return True

def is_solution(board):
    for row in range(9):
        for col in range(9):
            if isinstance(board[row][col], list):
                return False
    for row in range(9):
        for col in range(9):
            digit = board[row][col]
            if not verify(board,row,col,digit):
                return False  
    return True

def prepare():
    global sudoku
    print("The Sudoku:")
    display(sudoku)
    print("")
    global board
    board = [[0 for i in range(9)] for j in range(9)]
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] != 0:
                board[row][col] = sudoku[row][col]
            if sudoku[row][col]  == 0:
                board[row][col] = [i + 1 for i in range(9)]

def clean():
    global board
    for row in range(9):
        for col in range(9):
            if isinstance(board[row][col],list):
                board[row][col] = 0

def is_possible(row,col,digit):
    global board
    for i in range(9):
        if isinstance(board[row][i],int):
            if board[row][i] == digit:
                return False
    for j in range(9):
        if isinstance(board[j][col],int):
            if board[j][col] == digit:
                return False
    box_row = (row//3)*3
    box_col = (col//3)*3
    for i in range(3):
        for j in range(3):
            if isinstance(board[box_row+i][box_col+j],int) and board[box_row+i][box_col+j] == digit:
                return False    
    return True

def helper():
    global count
    global board
    flag = False
    count += 1
    for row in range(9):
        for col in range(9):
            if isinstance(board[row][col],list):
                for i in range(len(board[row][col])):
                    digit = board[row][col][i]
                    if not is_possible(row,col,digit):
                        board[row][col][i] = 0
                        flag = True
    removeZeros()
    update()
    if flag:
        helper()
    elif is_solution(board):
        pass
    elif not is_solution(board):
        flag = naked_single_box()
        if flag:
            helper()
        flag = naked_single_col()
        if flag:
            helper()
        flag = naked_single_row()
        if flag:
            helper()
        flag = naked_pairs_row()
        if flag:
            helper()
        flag = naked_pairs_col()
        if flag:
            helper()

def naked_single_box():
    flag = False
    global board
    for row in range(9):
        for col in range(9):
            box_row = (row//3)*3
            box_col = (col//3)*3
            counter = [0] * 9
            unique = []
            for i in range(3):
                for j in range(3):
                    if isinstance(board[box_row+i][box_col+j],list):
                        for k in range(len(board[box_row+i][box_col+j])):
                            digit = board[box_row+i][box_col+j][k]
                            counter[digit - 1] += 1
            for i in range(len(counter)):
                if counter[i] == 1:
                    unique.append(i + 1)
            for i in range(3):
                for j in range(3):
                    if isinstance(board[box_row+i][box_col+j],list) and len(set(board[box_row+i][box_col+j]) & set(unique)) == 1:
                        unique_digit = list(set(board[box_row+i][box_col+j]) & set(unique))[0]
                        for k in range(len(board[box_row+i][box_col+j])):
                            if board[box_row+i][box_col+j][k] != unique_digit:
                                board[box_row+i][box_col+j][k] = 0
                                flag = True
    removeZeros()
    update()
    return flag

def naked_single_row():
    flag = False
    global board
    for row in range(9):
        counter = [0] * 9
        unique = []
        for col in range(9):
            if isinstance(board[row][col],list):
                for i in range(len(board[row][col])):
                    digit = board[row][col][i]
                    counter[digit - 1] += 1
        for i in range(len(counter)):
            if counter[i] == 1:
                unique.append(i + 1)
        for col in range(9):
            if isinstance(board[row][col],list) and len(set(board[row][col]) & set(unique)) == 1:
                unique_digit = list(set(board[row][col]) & set(unique))[0]
                for i in range(len(board[row][col])):
                    if board[row][col][i] != unique_digit:
                        board[row][col][i] = 0
                        flag = True
    removeZeros()
    update()
    return flag

def naked_single_col():
    flag = False
    global board
    for row in range(9):
        counter = [0] * 9
        unique = []
        for col in range(9):
            if isinstance(board[col][row],list):
                for i in range(len(board[col][row])):
                    digit = board[col][row][i]
                    counter[digit - 1] += 1
        for i in range(len(counter)):
            if counter[i] == 1:
                unique.append(i + 1)
        for col in range(9):
            if isinstance(board[col][row],list) and len(set(board[col][row]) & set(unique)) == 1:
                unique_digit = list(set(board[col][row]) & set(unique))[0]
                for i in range(len(board[col][row])):
                    if board[col][row][i] != unique_digit:
                        board[col][row][i] = 0
                        flag = True
    removeZeros()
    update()
    return flag

                          
def naked_pairs_row():
    flag = False
    for row in range(0,5):
        for col in range(9):
            unique = []
            protect_col = 0
            if isinstance(board[row][col],list) and len(board[row][col]) == 2:
                for other_col in range(9):
                    if other_col != col and isinstance(board[row][other_col],list) and len(board[row][other_col]) == 2 and board[row][other_col] == board[row][col]:
                        for i in range(len(board[row][other_col])):
                                unique.append(board[row][col][i])
                        protect_col = other_col
                for target_col in range(9):
                    if isinstance(board[row][target_col],list) and target_col != col and target_col != protect_col:
                        for i in range(len(board[row][target_col])):
                            for j in unique:
                                if board[row][target_col][i] == j:
                                    board[row][target_col][i] = 0
                                    flag = True
    removeZeros()
    update()
    return flag

def naked_pairs_col():
    flag = False
    for row in range(0,5):
        for col in range(9):
            unique = []
            protect_col = 0
            if isinstance(board[col][row],list) and len(board[col][row]) == 2:
                for other_col in range(9):
                    if other_col != col and isinstance(board[other_col][row],list) and len(board[other_col][row]) == 2 and board[other_col][row] == board[col][row]:
                        for i in range(len(board[other_col][row])):
                                unique.append(board[col][row][i])
                        protect_col = other_col
                for target_col in range(9):
                    if isinstance(board[target_col][row],list) and target_col != col and target_col != protect_col:
                        for i in range(len(board[target_col][row])):
                            for j in unique:
                                if board[target_col][row][i] == j:
                                    board[target_col][row][i] = 0
                                    flag = True
    removeZeros()
    update()
    return flag

def backtrack_possible(row,col,digit):
    global bt_board
    for i in range(0,9):
        if bt_board[row][i] == digit:
            return False
    for i in range(0,9):
        if bt_board[i][col] == digit:
            return False
    box_row = (row//3)*3
    box_col = (col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if bt_board[box_row+i][box_col+j] == digit:
                return False    
    return True

def solve():
    global bt_board
    global bt_count
    global total_solutions
    global valid_sudoku
    bt_count += 1
    for row in range(9):
        for col in range(9):
            if bt_board[row][col] == 0:
                for digit in range(1,10):
                    if backtrack_possible(row,col,digit):
                        bt_board[row][col] = digit
                        solve()
                        bt_board[row][col] = 0  #Backtrack step
                return
    if is_solution(bt_board):
        total_solutions += 1
        if total_solutions > 1:
            valid_sudoku = False
        else:
            print("")
            print("The Solution:")
            display(bt_board)

###################
### DRIVER CODE ###
###################

sudoku = []
board = []
count = 0
bt_count = 0
total_solutions = 0
valid_sudoku = True

print("")
print("---How to manually enter the sudoku---")
print("Enter values from left to right, top to bottom, with 0 for unfilled cells.")
print("Example: 103450789120456709(...)")
print("This would represent row 1 with cells 2 and 6 empty, and row 2 with cells 3 and 8 empty.")
print("")

while True:
    sudoku_string = str(input("Input sudoku: "))
    if len(sudoku_string) == 81 and sudoku_string.isdecimal():
        break
    else:
        print("Try again.")
form_board(sudoku_string)

print("")

prepare()
begin = time.perf_counter()
helper()
end = time.perf_counter()
helper_time = end - begin

clean()
bt_board = board

begin = time.perf_counter()
solve()
end = time.perf_counter()
backtracker_time = end - begin

if bt_count == 1:
    print("")
    print("Solved without backtracking.")
    print("Tried " + str(count) + " times. Elapsed: " + str((end - begin)*1000) + " ms.")
if bt_count > 1:
    print("")
    print("Solved with backtracking.")
    print("Tried " + str(bt_count) + " times. Elapsed: " + str(((backtracker_time) + helper_time)*1000) + " ms.")
if not valid_sudoku:
    print("")
    print("This sudoku has " + str(total_solutions) + " solutions. It is not valid. The first solution found was displayed and the elapsed time reflects the time taken to compute every solution.")

