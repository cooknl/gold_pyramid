__author__ = 'Cooks'



def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    rows = len(pyramid)

    #Seed every path as an int, since the bits of the integer will cover every available path

    paths = [[int(x)] for x in range(2**(rows-1))]#[[0 for x in range((rows-1))] for x in range((rows-1)**2)]

    #Use bitwise operators!

    #Iterate over the seeds
    for int_path in paths:
        #Copy the seed to the seed variable
        seed = int_path[0]
        #Replace the seed with the first value from the pyramid
        int_path[0] = pyramid[0][0]
        #Initiate a column variable with 0. This will be used to keep up with the "left/right" choices
        col = 0
        #Iterate over the rows
        for row in range(1,rows):
            #Add the current least significant bit from the seed integer to the current value of the column
            # "0" = left and "1" = right
            col += seed & int(1)
            #bitshift the seed for the next row
            seed = seed >> 1
            #Append the value from pyramid in the given row/col to the int_path
            int_path.append(pyramid[row][col])
    return max([sum(x) for x in paths])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
