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
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.



# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.
if __name__ == "__main__":
    # unit tests
    # merge unit tests
    pass
    # provided.play_game(mc_move, NTRIALS, False)
    # poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
