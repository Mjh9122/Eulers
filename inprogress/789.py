import random
import numpy as np
from tqdm import tqdm

def find_cost(l:list) -> int:
    cost = 0
    for i, j in tqdm(enumerate(l)):
        if i % 2 == 1:
            cost += int(j * l[i+1] % p)
    return cost

p = 2_000_000_011



nums = np.empty(2_000_000_010, dtype=np.int32)
for i in tqdm(range(p - 1)):
    nums[i] = i
print("made_nums")

random.shuffle(nums)
print("shuffled_nums")

end = False
while not end:
    end = True
    for i, num1 in enumerate(nums):
        for num2 in nums[:i]:
print(find_cost(nums))
