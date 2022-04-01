# Maximize it!


# NOTE TO MYSELF: Code first, optimize later.

# Restrictions:
# K in range(1, 7)
# M in range(1, 1000)
# N in range(1, 7)
# numbers in list in range(1,1e9)

# Goal: choose an element in each list
# that maximizes the sum modulo M
# function to maximize: (x1**2 + ... + xk**2)%M

from itertools import product

if __name__ == '__main__':
    (K,M) = tuple(map(int, input().split()))
    lists = (list(map(int, input().split()))[1:] for _ in range(K))  
    all_mods = [[((x%M)**2)%M for x in l] for l in lists]
    kuplets = list(product(*all_mods))
    print(max(list(map(lambda x: sum(x)%M, kuplets))))


    # N = (list(map(int, input().split()))[1:] for _ in range(K))
    # results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
    # print(max(results))

