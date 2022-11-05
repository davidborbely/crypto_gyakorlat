import itertools


def get_next_element(num):
    # we square to get 2N digits, if not 2N digits then pad at the front. Return middle 6 digits
    return  int(str(num*num).zfill(12)[3:-3])

# getting fixpoints is straightforward
# generate list of numbers to go through: actually numbers from 0 to 999999, because 0 is 000000, 1 is 000001, etc.
fixpoints = set()
for seed in range(1000000):
    if seed == get_next_element(seed):
        fixpoints.add(seed)

print(f'These are the fixpoints {sorted(fixpoints)}')

# getting longest cycle: brute force approach might take a bit long
seqlength = dict()
for seed in range(1000000):
    seq = {seed}
    nextelem = get_next_element(seed)
    while nextelem not in seq:
        seq.add(nextelem)
        nextelem = get_next_element(nextelem)
    seqlength[seed] = len(seq)

# Actually, on my pc it runs in 2 minutes, so I won't bother making a more efficient solution (although I am sure it would be possible)

maxcycle = sorted(seqlength.items(), key=lambda x:x[1], reverse=True)[0] # get longest cycle length
print(f'The longest cycle length was {maxcycle[1]}, and it was achieved with the starting point of {maxcycle[0]}')