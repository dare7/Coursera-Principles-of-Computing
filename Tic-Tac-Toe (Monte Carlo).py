"""
Monte Carlo Tic-Tac-Toe Player
"""
__author__ = 'dare7'

import random
try:
    import poc_ttt_gui
except ImportError:
    import ext.poc_ttt_gui as poc_ttt_gui
try:
    import poc_ttt_provided
except ImportError:
    import ext.poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 500        # Number of trials to run
SCORE_CURRENT = 10.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.


def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by making random moves, alternating between players.
    The function should return when the game is over.
    The modified board will contain the state of the game, so the function does not return anything.
    In other words, the function should modify the board input
    :param board: ttt board for current game
    :param player: AI player
    :return: None, modifies input board
    """
    if player == 2:
        opponent = 3
    else:
        opponent = 2

    while board.check_win() not in (2, 3) and len(board.get_empty_squares()) > 0:
        move_player = random.randrange(len(board.get_empty_squares()))
        board.move(board.get_empty_squares()[move_player][0], board.get_empty_squares()[move_player][1], player)
        #print(board)
        if board.check_win() not in (2, 3) and len(board.get_empty_squares()) > 0:
            move_opponent = random.randrange(len(board.get_empty_squares()))
            board.move(board.get_empty_squares()[move_opponent][0], board.get_empty_squares()[move_opponent][1], opponent)
            #print(board)


def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board,
    a board from a completed game, and which player the machine player is.
    The function should score the completed board and update the scores grid.
    As the function updates the scores grid directly, it does not return anything,
    :param scores: input score table
    :param board: input TTT table after endgame
    :param player: AI player
    :return: NONE, modifies scores table
    """
    if player == 2:
        opponent = 3
    else:
        opponent = 2
    # iterate through result of finished game
    for dummy_row in range(board.get_dim()):
        for dummy_col in range(board.get_dim()):
            # scoring if we win
            if board.check_win() == player:
                if board.square(dummy_row, dummy_col) == player:
                    scores[dummy_row][dummy_col] += SCORE_CURRENT
                elif board.square(dummy_row, dummy_col) == opponent:
                    scores[dummy_row][dummy_col] -= SCORE_OTHER
            # scoring if opponent wins
            elif board.check_win() == opponent:
                if board.square(dummy_row, dummy_col) == player:
                    scores[dummy_row][dummy_col] -= SCORE_CURRENT
                elif board.square(dummy_row, dummy_col) == opponent:
                    scores[dummy_row][dummy_col] += SCORE_OTHER
            #if board.square(dummy_row, dummy_col) == 1:
            #    scores[dummy_row][dummy_col] = 0


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the maximum score
    and randomly return one of them as a (row, column) tuple.
    :param board: input TTT board for current game
    :param scores: input scores table
    :return: coordinate of cell of max weight (random if there are multiple)
    """
    maxed = {}
    # get all empty cells
    for dummy_row in range(board.get_dim()):
        for dummy_col in range(board.get_dim()):
            if board.square(dummy_row, dummy_col) == 1:
                maxed[(dummy_row, dummy_col)] = scores[dummy_row][dummy_col]
    if len(board.get_empty_squares()) > 0:
        # get max emty cell score
        maxval = max(list(maxed.values()))
        #print(maxval)
        max_list = []
        # make a list of max empty score cells
        for dummy_key, dummy_val in list(maxed.items()):
            if dummy_val == maxval:
                #print(dummy_key, dummy_val)
                max_list.append(dummy_key)
        result = max_list[random.randrange(len(max_list))]
        return result

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and the number of trials to run.
     The function should use the Monte Carlo simulation described above to return a move for the machine player
      in the form of a (row, column) tuple.
    :param board: the TTT board
    :param player:  AI player
    :param trials:  number of trials for Monte Carlo simulation
    :return: best move based on Monte Carlo simulation
    """
    mc_board = board.clone()
    scores = [[0 for dummy_col in range(mc_board.get_dim())] for dummy_row in range(mc_board.get_dim())]
    for dummy_game in range(trials):
        mc_trial(mc_board, player)
        if mc_board.check_win() in (2,3):
            mc_update_scores(scores, mc_board, player)
        mc_board = board.clone()
    #print(scores)
    return get_best_move(board,scores)



def monte_main():
    """
    test function
    :return:
    """
    board_size  = 3
    current_player = 2
    board = provided.TTTBoard(board_size)
    #scores = [[0 for dummy_col in range(board_size)] for dummy_row in range(board_size)]
    #mc_trial(board, current_player)
    #mc_update_scores(scores, board, current_player)
    #print(scores)
    #get_best_move(board, scores)
    #print(mc_move(board, current_player, NTRIALS))


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.
if __name__ == "__main__":
    # unit tests
    # merge unit tests
    #monte_main()
    #provided.play_game(mc_move, NTRIALS, False)
    poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
