from scipy.stats import bernoulli, uniform # pip install scipy

p = uniform.rvs(loc=0.4, scale=0.2, size=1) # generate an uniform rv between 0.4 and 0.6
source = bernoulli(p)

# Simulate a fair coin toss using this source
 # I've used a simple approach by John von Neumann: National Bureau of Standards, Applied Math Series, vol. 12. 1951, pp. 36-38.
 # throw twice, whenever HT (10) output H, whenever TH output T. Otherwise repeat
 # see article by Jakobsson et al. for more efficient approaches http://markus-jakobsson.com/papers/jakobsson-ieeeit00.pdf

def make_unbiased(source):
    while True:
        first = source.rvs(1)
        second = source.rvs(1)
        if first == 1 and second == 0:
            return 1
        elif first == 0 and second == 1:
            return 0

print(f'p={p}')
# test if original source is unbiased
n=10000
success=0
for i in range(n):
    success += source.rvs(1)
print(f'Trials with biased source: {success/n}')

# test if we could make it unbiased with Neumann's approach
success = 0
for i in range(n):
    success += make_unbiased(source)
print(f'Trials with Neumann\'s method: {success/n}')

# how can we convert this to a 6-sided die?
# the essence of a fair die is that all 6 sides are chosen with equal probability
# after some brainstorming:
 # toss a "fair" coin thrice with Neumann's approach. 8 outcomes are possible, all with equal probability:
 # H H H, H H T, H T H, T H H, T T H, T H T, H T T, T T T
 # let the first 6 of these correspond to each side of the die, and in case of the latter 2, repeat the experiment
def dieify(random_function, *args):
    while True:
        first = random_function(*args)
        second = random_function(*args)
        third = random_function(*args)
        if first == 1 and second == 1 and third == 1:
            return 1
        elif first == 1 and second == 1 and third == 0:
            return 2
        elif first == 1 and second == 0 and third == 1:
            return 3
        elif first == 0 and second == 1 and third == 1:
            return 4
        elif first == 0 and second == 0 and third == 1:
            return 5
        elif first == 0 and second == 1 and third == 0:
            return 6

# now we have the die, lets test it:
num_1 = num_2 = num_3 = num_4 = num_5 = num_6 = 0
for i in range(n):
    result = dieify(make_unbiased, source)
    if result == 1:
        num_1 += 1
    elif result == 2:
        num_2 += 1
    elif result == 3:
        num_3 += 1
    elif result == 4:
        num_4 += 1
    elif result == 5:
        num_5 += 1
    elif result == 6:
        num_6 += 1
print('Results of a die made out of Neumann\'s fair coin:')
print(f'P(1)={num_1/n}\nP(2)={num_2/n}\nP(3)={num_3/n}\nP(4)={num_4/n}\nP(5)={num_5/n}\nP(6)={num_6/n}\n')

# seems fair, lets try if we would do the same with the original biased source:
num_1 = num_2 = num_3 = num_4 = num_5 = num_6 = 0
for i in range(n):
    result = dieify(source.rvs, 1)
    if result == 1:
        num_1 += 1
    elif result == 2:
        num_2 += 1
    elif result == 3:
        num_3 += 1
    elif result == 4:
        num_4 += 1
    elif result == 5:
        num_5 += 1
    elif result == 6:
        num_6 += 1
print(f'Results of a die made out of the original biased source (p={p}):')
print(f'P(1)={num_1/n}\nP(2)={num_2/n}\nP(3)={num_3/n}\nP(4)={num_4/n}\nP(5)={num_5/n}\nP(6)={num_6/n}\n')
# we can see that these numbers are not perfectly balanced. Makes sense, for example if the original bernoulli's p was closer to 0.6, then the outcome 1 1 1 is likelier than otherwise
