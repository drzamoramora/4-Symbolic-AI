# problem: generate two groups, with different numbers
# group 1: 5 elements must sum 36
# group 2: 5 elements prod must be 360

import datetime
import functools
import operator
import random
import unittest
import genetic


# group of elements
geneset = [i + 1 for i in range(10)]
print("geneset",geneset)
print("")
startTime = datetime.datetime.now()

#  ================ WRAPPERS ================

def get_fitness(genes):
    group1Sum = sum(genes[0:5])
    group2Product = functools.reduce(operator.mul, genes[5:10])
    duplicateCount = (len(genes) - len(set(genes)))
    return Fitness(group1Sum, group2Product, duplicateCount)

class Fitness:
    def __init__(self, group1Sum, group2Product, duplicateCount):
        self.Group1Sum = group1Sum
        self.Group2Product = group2Product
        sumDifference = abs(36 - group1Sum)
        productDifference = abs(360 - group2Product)
        self.TotalDifference = sumDifference + productDifference
        self.DuplicateCount = duplicateCount

    def __gt__(self, other):
        if self.DuplicateCount != other.DuplicateCount:
            return self.DuplicateCount < other.DuplicateCount
        return self.TotalDifference < other.TotalDifference

    def __str__(self):
        return "sum: {} prod: {} dups: {}".format(
            self.Group1Sum,
            self.Group2Product,
            self.DuplicateCount)

#  ================ MAIN ================

parent = genetic._generate_parent(10, geneset, get_fitness)
print("parent:", parent.Genes, parent.Fitness)

child = genetic._mutate(parent, geneset, get_fitness)
print("child:", child.Genes, child.Fitness)



