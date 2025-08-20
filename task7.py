try:
    file = open('sample.txt', 'r')
    # read first line
    line1 = file.readline()
    print('The first line is:', line1)
    # read the second line
    line2 = file.readline()
    print('The second line is:', line2)
    file.close()
except FileNotFoundError:
    print('The above file mentioned does not exist!')

finally:
    print('Thank You.')
