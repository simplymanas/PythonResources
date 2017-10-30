import random


# gerenate random between 0 and 1.0
print(random.random())

#range
print(random.uniform(1,50))

#from  a range

print(random.randint(1,50))

# from a range with a step of the lower bound

print(random.randrange(0, 101, 5))
print(random.randrange(0, 101, 5))

#pick a random element from a sequence

inputList = [4, 5, 6, 8, 9, 2]

print(random.choice(inputList))
