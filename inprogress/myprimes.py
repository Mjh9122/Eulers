class Primelist:
    def __init__(self):
        self.prime_list = []
        with open('..\\txts\\primes\\1st-million.txt') as f:
            lines = f.readlines()
            for l in lines:
                l = l.strip()
                l = l.split()
                self.prime_list.extend([int(p) for p in l if p != ''])
        with open('..\\txts\\primes\\2nd-million.txt') as f:
            lines = f.readlines()
            for l in lines:
                l = l.strip()
                l = l.split()
                self.prime_list.extend([int(p) for p in l if p != ''])