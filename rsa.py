import math
import sympy # pip install sympy

nums = []
factors = {}
with open('RSA_modulus3.TXT', 'r') as infile:
    for l in infile.readlines():
        nums.append(int(l))
        factors[int(l)] = set()

primes = set()
for i1 in nums:
    for i2 in nums:
        gcd = math.gcd(i1, i2)
        if sympy.isprime(gcd):
            primes.add(gcd)
            factors[i1].add(gcd)
            factors[i2].add(gcd)

print(len(primes))

with open('output.TXT', 'w') as outfile:
    for i in range(len(nums)):
        if len(factors[nums[i]]) == 0:
            outfile.write(f'Found no factors for {i+1}. num\n\n')
        else:
            outfile.write(f'Factors for {i+1}. num: {", ".join([str(num) for num in factors[nums[i]]])}\n\n')

