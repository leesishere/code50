"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = sum(row.count("X") for row in board)
    count_O = sum(row.count("O") for row in board)
    if count_X > count_O:
        return "O"
    elif count_X < count_O:
        return "X"
    else:
        return "X"  # X always goes first

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_positions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell not in ("X", "O"):
                empty_positions.add((i, j))

    return empty_positions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")

    i, j = action
    new_board = [row[:] for row in board]  # Create a deep copy of the board
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def max_value(board):
    # check for terminal state
    if terminal(board):
        return utility(board)
    # assign negative infinity to v
    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    # check for terminal state
    if terminal(board):
        return utility(board)
    # assign positive infinity to v
    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        best_value = -math.inf
        best_action = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    else:
        best_value = math.inf
        best_action = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action
        return best_action




def minimaxwin(board):
    """
    Returns the optimal action for the current player on the board.
    """
    win = None
    block = None

    if terminal(board):
        return None


    #if we are the first player our optimal move is to take the center
    if board == [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]:
        return (1,1)

    open_positions = actions(board)

    # check for the win and block!
    # Check row
    for i in range(3):
        if board[i][0] == board[i][1] != EMPTY:
            if board[i][2] == EMPTY:
                if board[i][0] == player(board):
                    win = (i,2)
                else:
                    block = (i,2)
        if board[i][0] == board[i][2] != EMPTY:
            if board[i][1] == EMPTY:
                if board[i][0] == player(board):
                    win = (i,1)
                else:
                    block = (i,1)
        if board[i][1] == board[i][2] != EMPTY:
            if board[i][0] == EMPTY:
                if board[i][1] == player(board):
                    win = (i,0)
                else:
                    block = (i,0)

        # Check column
        if board[0][i] == board[1][i] != EMPTY:
            if board[2][i] == EMPTY:
                if board[0][i] == player(board):
                    win = (2,i)
                else:
                    block = (2,i)
        if board[0][i] == board[2][i] != EMPTY:
            if board[1][i] == EMPTY:
                if board[0][i] == player(board):
                    win = (1,i)
                else:
                    block = (1,i)
        if board[1][i] == board[2][i] != EMPTY:
            if board[0][i] == EMPTY:
                if board[1][i] == player(board):
                    win = (0,i)
                else:
                    block = (0,i)
    # Check diagonal
        # Check diagonals
        if board[0][0] == board[1][1] != EMPTY:
            if board[2][2] == EMPTY:
                return (2,2)
        if board[0][0] == board[2][2] != EMPTY:
            if board[1][1] == EMPTY:
                if board[0][0] == player(board):
                    win = (1,1)
                else:
                    block = (1,1)
        if board[1][1] == board[0][0] != EMPTY:
            if board[2][2] == EMPTY:
                if board[1][1] == player(board):
                    win = (2,2)
                else:
                    block = (2,2)
        if board[1][1] == board[2][2] != EMPTY:
            if board[0][0] == EMPTY:
                if board[1][1] == player(board):
                    win = (0,0)
                else:
                    block = (0,0)
        if board[0][2] == board[1][1] != EMPTY:
            if board[2][0] == EMPTY:
                if board[0][2] == player(board):
                    win = (2,0)
                else:
                    block = (2,0)
        if board[0][2] == board[2][0] != EMPTY:
            if board[1][1] == EMPTY:
                if board[0][2] == player(board):
                    win = (1,1)
                else:
                    block = (1,1)
        if board[1][1] == board[2][0] != EMPTY:
            if board[0][2] == EMPTY:
                if board[1][1] == player(board):
                    win = (0,2)
                else:
                    block = (0,2)
        if board[1][1] == board[0][2] != EMPTY:
            if board[2][0] == EMPTY:
                if board[1][1] == player(board):
                    win = (2,0)
                else:
                    block = (2,0)

    if win is not None:
        return win
    if block is not None:
        return block
    action = random.choice(list(open_positions))
    #action = min(open_positions)
    return action

