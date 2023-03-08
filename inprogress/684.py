from multiprocessing import Pool
from tqdm import tqdm
import timeit
import math

p = 1_000_000_007
pows = [10]
for i in range(100):
    pows.append(pows[-1] ** 2 % p)

def mod_min_dig_sum(x):
    y = (x // 9) % p
    z = x % 9
    total = (z * (10 ** y)% p)
    total += (10 ** y - 1) % p
    return total % p

def mod_min_dig_sum_with_bin(x):
    y = (x // 9)
    z = x % 9

    exp = str(bin(y))[2:][::-1]
    mod = 1
    for i in range(len(exp)):
        if exp[i] == "1":
            mod *= pows[i]
        mod %= p


    total = (z * mod)
    total += (mod - 1) % p
    return total % p
    

def by_nines_sum(x):
    n = (x // 9) % p
    left = x % 9
    num = 0
    if n > 0:
        num = (6 * (10 ** n) )%p - (6 + (9 * n) % p)
    for i in range(x-left + 1, x+ 1):
        num += mod_min_dig_sum(i)
        num %= p
    return num % p


def by_nines_with_bin(x):
    n = (x // 9)
    left = x % 9
    num = 0
    exp = str(bin(n))[2:][::-1]
    mod = 1
    for i in range(len(exp)):
        if exp[i] == "1":
            mod *= pows[i]
        mod %= p
    if n > 0:
        num = (6 * mod) % p - (6 + (9 * n) % p)
    for i in range(x-left + 1, x+ 1):
        num += mod_min_dig_sum_with_bin(i)
        num %= p
    return num % p



if __name__ == "__main__":
    fibs = [1, 1]
    for i in range(88):
        fibs.append(fibs[-2]+fibs[-1])
    print(fibs)
    print(by_nines_with_bin(20))
    
    with Pool() as pool:
        r = list(tqdm(pool.imap(by_nines_with_bin, fibs), total=90))
        print(sum(r[1:]) % p)
