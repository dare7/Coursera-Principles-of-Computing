"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
online version on python 2.6: http://www.codeskulptor.org/#user40_PGW5PxAOeVtmyaV_0.py
"""

__author__ = 'dare7'
try:
    import codeskulptor
except ImportError:
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor
try:
    import poc_simpletest
except ImportError:
    import ext.poc_simpletest as poc_simpletest
#import poc_holds_testsuite

codeskulptor.set_timeout(20)
# Used to increase the timeout, if necessary


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for dummy_partial_sequence in answer_set:
            for dummy_item in outcomes:
                new_sequence = list(dummy_partial_sequence)
                new_sequence.append(dummy_item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    #print(answer_set)
    return answer_set

def gen_sorted_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    unsorted = gen_all_sequences(outcomes, length)
    for dummy_el in unsorted:
        answer_set.add(sorted(dummy_el))
    return answer_set


def score(hand_in):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    result = 0
    for dummy_dice in hand_in:
        temp_score = hand_in.count(dummy_dice) * dummy_dice
        if temp_score > result:
            result = temp_score
    return result

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes = list(range(num_die_sides+1))[1:]
    all_hands = gen_all_sequences(outcomes, num_free_dice)
    result = 0.0
    for dummy_hand in all_hands:
        result += score(tuple(list(dummy_hand)+ list(held_dice)))
    result /= (len(all_hands))
    return result

def gen_all_holds(hand_in):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = set([()])
    if len(hand_in) == 0:
        return answer_set
    else:
        temp_hands = hand_in[:-1]
        #print("temp_hand", temp_hands)
        for dummy_each_tuple in gen_all_holds(temp_hands):
            answer_set.add(dummy_each_tuple)
            #print("each tuple", each_tuple, "hand", hand[-1])
            answer_set.add((dummy_each_tuple + (hand_in[-1],)))


    #print(answer_set)
    return answer_set


def strategy(hand_in, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    #expected_value(held_dice, num_die_sides, num_free_dice)
    #gen_all_holds(hand)
    #for dummy_idx in range(num_die_sides):
    #sides = list(range(num_die_sides))
    #all_holds = gen_all_holds(hand)
    result_score = 0.0
    result_hold = ()
    for dummy_hold in gen_all_holds(hand_in):
        temp_score = expected_value(dummy_hold, num_die_sides, len(hand_in) - len(dummy_hold))
        if temp_score > result_score:
            result_score = temp_score
            result_hold = dummy_hold
    #print("result score, hold hand", result_score, result_hold)
    return (result_score, result_hold)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    #num_die_sides = 6
    #hand = (1, 1, 1, 5, 6)
    #hand_score, hold = strategy(hand, num_die_sides)
    #print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)
    pass
    
if __name__ == "__main__":
    #run_example()
    #unit tests
    #hand = (1, 2, 3, 5, 6)
    #score(hand)
    #print(score((2, 2)))
    #print(expected_value((2, 2), 6, 2))
    #print(expected_value((),8,1))
    #print(strategy((1, 2), 6))
    test = poc_simpletest.TestSuite()
    # expected_value unit test
    test.run_test(score((2, 2)), 4, "score")
    test.run_test(expected_value((2, 2), 6, 2), 5.833333333333333, "expected")
    test.run_test(strategy((1, 2), 6), (5.055555555555555, ()), "strategy")
    test.report_results()
    #gen_all_sequences((1,2,3,4,5,6), 2)
    #gen_all_sequences(hand, 3)
    #gen_all_holds(hand)
    #import poc_holds_testsuite
    #poc_holds_testsuite.run_suite(gen_all_holds)
    #strategy((1,), 6)
    #run_example()
