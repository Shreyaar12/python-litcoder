# Problem Statement
# Sudoku board validation algorithm
# You have been tasked with developing an algorithm to validate a 9 x 9 Sudoku board. Your algorithm needs to verify the validity of the filled cells on the board, adhering to the following conditions:

# Every row should contain the numbers 1-9 exactly once, without repetition.
# Every column should contain the numbers 1-9 exactly once, without repetition.
# Each of the nine 3 x 3 sub-boxes within the grid should contain the numbers 1-9 exactly once, without repetition.

# Can you outline an algorithm or a step-by-step approach to determine if the given Sudoku board configuration is valid based on these conditions?

# Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

# Exercise-1

# Input :

# 9
# 5 3 . . 7 . . . .
# 6 . . 1 9 5 . . .
# . 9 8 . . . . 6 .
# 8 . . . 6 . . . 3
# 4 . . 8 . 3 . . 1
# 7 . . . 2 . . . 6
# . 6 . . . . 2 8 .
# . . . 4 1 9 . . 5
# . . . . 8 . . 7 9

# Output :

# YES

# Exercise-2

# Input:

# 9
# 5 3 . . 7 . . . .
# 5 . . 1 9 5 . . .
# . 9 8 . . . . 6 .
# 8 . . . 6 . . . 3
# 4 . . 8 . 3 . . 1
# 7 . . . 2 . . . 6
# . 6 . . . . 2 8 .
# . . . 4 1 9 . . 5
# . . . . 8 . . 7 9

# Output:
# NO
import sys

def isValidSudoku(board):
    cross3 = {}
    for i in range(3):
        for j in range(3):
            cross3 = {}
            for x in range(i*3, i*3+3):
                for y in range(j*3, j*3+3):
                    if x < len(board) and y < len(board[x]) and board[x][y] != '.':
                        if board[x][y] not in cross3:
                            cross3[board[x][y]] = ''
                        else:
                            return "NO"

    Big_Location = {"1x":{}, "2x":{}, "3x":{}, "4x":{}, "5x":{}, "6x":{}, "7x":{}, "8x":{}, "9x":{}, "1y":{}, "2y":{}, "3y":{}, "4y":{}, "5y":{}, "6y":{}, "7y":{}, "8y":{}, "9y":{}}
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] != '.':
                if x in Big_Location[board[x][y]+"x"] or y in Big_Location[board[x][y]+"y"]:
                    return "NO"
                else:
                    Big_Location[board[x][y]+"x"][x] = "f"
                    Big_Location[board[x][y]+"y"][y] = "f"
    return "YES"

def doSomething(input_val):
    # Assuming the input format is as described in the prompt
    board_str = input_val.split("\n")[1:-1]  # Exclude the first and last empty elements

    # Convert input lines into a list of lists
    board = [list(row.split()) for row in board_str]

    return isValidSudoku(board)



def take_multiline_input():
    lines = []
    for _ in range(10):
        line = input().strip()
        lines.append(line)
    return '\n'.join(lines)

inputVal = take_multiline_input()
outputVal = doSomething(inputVal)
print(outputVal)

