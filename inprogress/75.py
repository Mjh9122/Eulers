import math
import numpy as np
from tqdm import tqdm

from multiprocessing import pool

nums = [i for i in range(1_500_000)]
sqrs = [i ** 2 for i in nums]
set_sqrs = set(sqrs)


ones = set()
used = set()
for a in tqdm(range(1, 750_000)[::-1]):
    for b in range(1, a):
        if (c2 := a ** 2 + b ** 2) in set_sqrs:
            if (new := np.round((c2 ** .5) + b + a)) in ones:
                ones.remove(new)
            elif new not in used and new < 1_500_000:
                ones.add(new)
                used.add(new)
        if np.round((c2 ** .5) + b + a) > 1_500_000:
            break

print(len(ones))




