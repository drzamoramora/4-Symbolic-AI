import genetic as gen
import datetime

geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"
guess = "hello worrx"
target = "hello world"


# just prints data if a chromosome
def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(candidate.Genes, candidate.Fitness, timeDiff))

# display wrapper
def fnDisplay(candidate):
    startTime = datetime.datetime.now()
    display(candidate, startTime)

# the fitness function
# similar to the Levenshtein formula!
def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)

# Fitness function wrapper
def fnGetFitness(genes):
    return get_fitness(genes, target)

print("Fitness Example:", get_fitness(guess, target))
print("Fitness Example Wrapper:", fnGetFitness(guess))
print("")

# generate parent creates a NEW string with random digits.
chromo = gen._generate_parent(len(guess), geneset, fnGetFitness)
print("new chromosome", chromo.Genes, chromo.Fitness)

# mutation takes the genrated chromosome (string) and changes 1 random character
mutate = gen._mutate(chromo, geneset, fnGetFitness)
print("new mutation", mutate.Genes, mutate.Fitness)

# uncomment to test!
#target = "For I am fearfully and wonderfully made."

# main execution! this just generates random words until it finds the target...
best = gen.get_best(fnGetFitness, len(target), len(target), geneset, fnDisplay)
print(best)