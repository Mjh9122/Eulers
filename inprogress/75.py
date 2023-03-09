import math
import numpy as np
from tqdm import tqdm

from multiprocessing import pool

nums = [i for i in range(1_500_000)]
sqrs = [i ** 2 for i in nums]
set_sqrs = set(sqrs)


ones = set()
used = set()
for c in tqdm(range(1, 750_000)[::-1]):
    for b in range(1, c):
        if (a2 := c ** 2 - b ** 2) in set_sqrs:
            if math.sqrt(a2) < b:
                if (new := int(a2 ** .5) + b + c) in ones:
                    ones.remove(new)
                elif new not in used:
                    ones.add(new)
                    used.add(new)
            

print(len(ones))




