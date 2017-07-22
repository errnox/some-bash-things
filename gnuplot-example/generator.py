import random, sys

"""
Fills up a test file with random data.
"""


out_file = open('./finance.dat', 'r+')

for i in range(500):
    # for i in range(3):
    #     out_file.write(str(random.randrange(0, 500)) + '\t')
    # out_file.write('\n')

    for i in range(15):
        random_prefix = random.randrange(0, 9999)
        random_number = random.randrange(0, 500)
        out_file.write(str(random_prefix) + ',' + str(random_number) + ' ')
    out_file.write('\n')

out_file.close()

