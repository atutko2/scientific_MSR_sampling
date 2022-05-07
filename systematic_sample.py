import pandas as pd
import time
from random import seed
from random import randint
import sys
import random

seed = random.randrange(sys.maxsize)
random.seed(seed)


# general systematic sample

def systematic_sample(df, sample_size):
   
    # get the size of the population
    length_of_df = len(df)
    
    interval = int((length_of_df)/sample_size)
    
    # get a random number between 1 and population size / desired_sample_size
    # This is the start of the systematic sample
    value = randint(0, int((length_of_df)/sample_size))
    
    # get the systematic sample
    systematic_sample = []
    for _ in range(sample_size):
        systematic_sample.append(df.iloc[value])
        value += interval

    return seed, pd.DataFrame(systematic_sample)
