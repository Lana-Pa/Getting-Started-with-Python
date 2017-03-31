import random

for i in range(10):
    float_random= random.random() # returns random float number [0.0,1.0)
    int_random = random.randint(5,20) # returns random int from 5 to 20 (including)
    sequence = [1,2,3]
    rand_from_sequence = random.choice(sequence) # returns random element from sequence

    print rand_from_sequence
