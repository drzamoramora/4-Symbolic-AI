import datetime
import genetic

totalNumbers = 10
geneset = [i for i in range(100)]

#  ================ FITNESS OBJ ================
class Fitness:
    def __init__(self, numbersInSequenceCount, totalGap):
        self.NumbersInSequenceCount = numbersInSequenceCount
        self.TotalGap = totalGap

    def __gt__(self, other):
        if self.NumbersInSequenceCount != other.NumbersInSequenceCount:
            return self.NumbersInSequenceCount > other.NumbersInSequenceCount
        return self.TotalGap < other.TotalGap

    def __str__(self):
        return "{} Sequential, {} Total Gap".format(
            self.NumbersInSequenceCount,
            self.TotalGap)

#  ================ WRAPPERS ================
def get_fitness(genes):
    fitness = 1
    gap = 0

    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            fitness += 1
        else:
            gap += genes[i - 1] - genes[i]
    return Fitness(fitness, gap)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t=> {}\t{}".format(
        ', '.join(map(str, candidate.Genes)),
        candidate.Fitness,
        timeDiff))

def fnDisplay(candidate):
    display(candidate, startTime)

def fnGetFitness(genes):
    return get_fitness(genes)

# ================ MAIN ================

parent = genetic._generate_parent(totalNumbers, geneset, fnGetFitness)
print("parent:", parent.Genes, parent.Fitness)

child = genetic._mutate(parent, geneset, fnGetFitness)
print("child:", child.Genes, child.Fitness)