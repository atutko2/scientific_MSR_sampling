import pandas as pd
import time
from random import seed
from random import randint
import sys
import random

seed = random.randrange(sys.maxsize)
random.seed(seed)

#simple random sampling

def simple_random_sample(df, sample_size):
    
    length_of_df = len(df)
    random_sample = []
    
    for _ in range(sample_size):
        value = randint(0, length_of_df-1)
        result = df.iloc[value]
        random_sample.append(result)
    return seed, pd.DataFrame(random_sample)

