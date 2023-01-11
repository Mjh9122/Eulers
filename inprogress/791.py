import math
import numpy as np
# import matplotlib.pyplot as plt

# 1 <= a <= b <= c <= d <= n
n = 10000
total = 0
count = 0
for d in np.arange(n, 0, -1, dtype=np.float64):
    min_c, max_c = 0, d
    if (sqrt := 24 * d + 9) >= 0: 
        sqrt = math.sqrt(sqrt)
        min_c, max_c = (
            int(((3 * d + 3) - sqrt) / 3) - 1,
            int(((3 * d + 3) + sqrt) / 3) + 1,
        )
    for c in np.arange(min(d, max_c), max(min_c, 0), -1):
        if (
            sqrt := (2 * (1 + c + d)) ** 2
            - 8 * ((3 / 2) * c**2 - d * c + (3 / 2) * d**2 - d - c)
        ) >= 0:
            min_b, max_b = 0, c
            sqrt = math.sqrt(sqrt)
            min_b = int(((2 + 2 * c + 2 * d) - sqrt) / 4 - 0.0001)
        for b in np.arange(c, max(0, min_b), -1):
            # count += 1
            sum_max = d + c + 2 * b
            a = (1 + b + c + d
                - math.sqrt((-1 - b - c - d) ** 2
                + 6 * (b + c + d + b * c + b * d + c * d
                        - (3 / 2) * (b * b + c * c + d * d)))) / 3
            if not int(a) == a:
                continue
            elif 1 <= a <= b:
                total += a + b + c + d
                if total > 433494437:
                    total -= 433494437
 
print(total, count, count / n**2)