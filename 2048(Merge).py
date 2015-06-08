"""
Merge function for 2048 game.
Online version(python 2.6): http://www.codeskulptor.org/#user40_wSOQzDHb73kFAo3.py
"""
__author__ = 'dare7'

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # local variables
    zero_shift = []
    number_merge = []
    result = []
    blank = 0
    cache = 0

    # initializing blank list
    for idx in range(len(line)):
        number_merge.append(0)

    # shifting zeroes in initial list
    for val in line:
        if val != 0:
            zero_shift.append(val)
        else:
            blank += 1

    for idx in range(blank):
        zero_shift.append(0)

    # merging values in shifted list
    for idx, val in enumerate(zero_shift):
        #print("cache:", cache, "value:", val, "index:", idx, "shift_list", zero_shift, "merge_list", number_merge)
        if val == cache and val != 0:
            number_merge[idx-1] = val*2
            number_merge[idx] = 0
            cache = 0
        else:
            number_merge[idx] = val
            cache = val

    # shifting zeroes in merged list
    blank = 0
    for val in number_merge:
        if val != 0:
            result.append(val)
        else:
            blank += 1

    for idx in range(blank):
        result.append(0)

    return result

if __name__ == "__main__":
    # tests
    print("should return [4, 4, 0, 0]",merge([2, 0, 2, 4]))
    print("should return [4, 0, 0, 0]",merge([0, 0, 2, 2]))
    print("should return [4, 0, 0, 0]",merge([2, 2, 0, 0]))
    print("should return [4, 4, 2, 0, 0]",merge([2, 2, 2, 2, 2]))
    print("should return [8, 32, 8, 0]",merge([8, 16, 16, 8]))