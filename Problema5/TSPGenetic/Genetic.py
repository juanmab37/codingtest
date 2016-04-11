import Graph
import copy
from heapq import *
from random import *
import random

def flip(listA, i, j):

    #flips a subpath within the path
    if (i < j):
        listB = listA[:i]
        listB.extend(reversed(listA[i:j]))
        listB.extend(listA[j:])
    else:
        listB = listA[:j]
        listB.extend(reversed(listA[j:i]))
        listB.extend(listA[i:])

    return listB

def evaluatePath(aGraph, path):
    distance = 0

    #loops over the path and finds the distance traveled
    for i in range(0, len(path) - 1):
        distance += aGraph.getAt(path[i], path[i + 1])
    distance += aGraph.getAt(path[-1], path[0])
    return distance

def main():
    '''
    Find a close solution to traveling salesman problem
    through genetic inver-over algorithm
    '''

    #variable delcaration
    populationSize = 100
    probability = .07
    filename = "cites.tsp"
    aGraph = Graph.fromTSPFile(filename)
    #aGraph = Graph.Graph(["one","two","three","four","five","six"],3,1.0)
    population = []
    path = aGraph.getNames()
    stable = 0
    repeat = True
    bestDistance = None
    oldBestDistance = None
    bestPath = []
    oldBestPath = []
    inversions = 0
    iterations = 0

    #Build the population
    for i in range(0, populationSize):
        shuffle(path)
        population.append(copy.copy(path))

    print aGraph

    #Loop until same results occur 10 times across total population
    while (stable < 10):

        iterations = iterations + 1
 
        #For each path, pick a city and flip sub paths to another city
        for i in range (0, len(population)):
            testPath = copy.copy(population[i])

            city = testPath[random.randint(0, len(testPath) - 1)]
            repeat = True;
            
            bestDistance = None

            #While swaps can be made
            while repeat:

                #Possibly mutate and pick a city at random
                if (random.random() <= probability):
                    otherCity = testPath[random.randint(0, len(testPath) - 1)]
                    while (city == otherCity or (city == 6 and otherCity == 15) or (city == 13 and otherCity == 3) or (city == 11 and otherCity == 18) or (city == 1 and otherCity == 7) or (city == 9 and otherCity == 16)):
                        otherCity = testPath[random.randint(0, len(testPath) - 1)]

                #Otherwise look for solution from another path at random
                #By finding a node next to city
                else:
                    otherPath = population[random.randint(0, len(population) - 1)]

                    #If city is at the end of the other path, cycle to the first node
                    if (otherPath.index(city) == (len(otherPath) - 1)):
                        otherCity = otherPath[0]

                    #Else, grab the next city
                    else:
                        otherCity = otherPath[otherPath.index(city) + 1]

                #If the cities to flip around are next to eachother, stop
                if ((testPath.index(otherCity) + 1 == testPath.index(city)) or
                    (testPath.index(otherCity) - 1 == testPath.index(city)) or
                    ((testPath.index(otherCity) == 0) and (testPath.index(city) == len(testPath) - 1)) or
                    ((testPath.index(city) == 0) and (testPath.index(otherCity) == len(testPath) - 1))):
                    repeat = False

                #Otherwise, flip the subpath
                else:
                    testPath = copy.copy(flip(testPath, testPath.index(city), testPath.index(otherCity)))
                    inversions = inversions + 1

            #Updates the path to faster version if needed
            if (evaluatePath(aGraph, testPath) <= evaluatePath(aGraph, population[i])):
                population[i] = copy.copy(testPath)

            #Updates the fastest distance and path for this interation of the
            #population if needed
            if (bestDistance == None) or (evaluatePath(aGraph, population[i]) < bestDistance):
                bestDistance = evaluatePath(aGraph, population[i])
                bestPath = copy.copy(population[i])

        #Updates the fastest distance and path for all iterations of the population
        #so far, if needed.
        if (oldBestDistance == None) or (bestDistance < oldBestDistance):
            oldBestDistance = bestDistance
            oldBestPath = copy.copy(bestPath)
            stable = 0

        #If no faster path is found increment the stable counter (exit condition)
        else:
            stable += 1
            
        print "working"
    
    print "Best Distance Found: "
    print oldBestDistance
    print "Best Path Found: "
    print oldBestPath
    print "Inversions: "
    print inversions
    print "Iterations: "
    print iterations
    
main()
