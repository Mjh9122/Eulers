import timeit
import math
from tqdm import tqdm 

limit = 800800**800800
log_limit = math.log2(limit)
count = 0 

with open('../Eulers-/txts/primes/1st-million.txt') as prime_file:
    primes = prime_file.read().strip('\n').split(" ")
    primes = [int(n) for n in primes if n != "" and n != "\n"]
    for i, p1 in tqdm(enumerate(primes[::-1]), total = 1_000_000):
        if p1 < log_limit:
            for p2 in primes[:i]:
                if p1 != p2:
                    if p1 ** p2 * p2 ** p1 < limit:
                        count += 1
                    else:
                        break
print(count//2)