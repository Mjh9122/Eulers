# Michael Holtz
# Lazy Python Solution for Project Euler Problem #686
# All code is mine

import math

if __name__ == "__main__":
    string = "123"
    num = 2
    count = 0
    power = 1
    digits = 1 + int(power * math.log10(2))
    while count < 678910:
        power += 1
        digits = 1 + int(power * math.log10(2))
        first = int(10 ** (power * math.log10(2) - digits + 3))
        if first == 123:
            count += 1
            if not count % 1000:
                print(count, power)
print(power, count)