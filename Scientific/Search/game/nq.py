import random
import operator as op
import numpy as np
from itertools import combinations
import math
from game import drawboard as db
import time
import os

clear = lambda: os.system('cls')

class queen:
    def __init__ (self, n, population_size, threshold=15):
        self.n_queen = n
        self.population_size = population_size
        self.threshold = threshold
        self.initsolution = self.generateRandomSolution(population_size)
        self.maximumconflict = self.ncr(n, 2)        
        self.fitnessscores = self.getfitness()
        self.triedsolutions = []

        self.seqs = []
        self.fitnesses = []


    def makeitrain(self):
        iteration = 1
        starttime = time.time()
        while not self.solutionfound():
            print ('Iteration # ' + str(iteration))
            iteration += 1            
            print ('Current sequences: ')
            for seq in self.initsolution:
                print(seq)
            print ('Current fitness scores: ')            
            print (self.fitnessscores)
            print ('Making natural selection')            
            self.naturalselection()
            #if after natural selection at least two of current sequence passes minimum requirement create new possible sequences.
            if len(self.initsolution) < 2:
                print('None of current sequences passed natural selction.')
                self.initsolution = self.generateRandomSolution(self.population_size)
            print ('After natural selection Current sequences: ')
            for seq in self.initsolution:
                print(seq)                           
            print('Crossing over.... ')
            self.crossover()
            self.fitnessscores = self.getfitness()

            mx = -1
            for score in self.fitnessscores:
                if score > mx:
                    mx = score
            # if score == self.maximumconflict:
            if mx != -1:
                self.seqs.append(self.initsolution[self.fitnessscores.index(mx)])
                self.fitnesses.append(mx)
        duration = time.time() - starttime
        clear()
        print("===================================================")
        print("Summary")
        print("Number of Queen: " + str(self.n_queen))        
        print("Total generation: " + str(iteration))
        print("Population per generation: " + str(self.population_size))
        print("Required time: " + str(duration) + 's')
        print("Total population tried/mutated: " + str(len(self.triedsolutions)))
        for score in self.fitnessscores:
            if score == self.maximumconflict:
                print("solution found.")
                print(self.initsolution[self.fitnessscores.index(score)])                
                db.init(1, 80, self.seqs, self.n_queen, self.fitnesses)
                break



    def crossover(self):
        #putting current sequences into log
        # self.uniquentries(self.initsolution)
        #make couples of solution to crossover
        solutioncouples = self.getrandomcouples(self.population_size/2)
        crossoveredsolutions = []
        for x in solutioncouples:
            crossoveredsolutions.extend(self.cross(x))
        print ("New Sequences: Crossover")
        for seq in crossoveredsolutions:
            print(seq)
        newsequences = [self.mutate(x) for x in crossoveredsolutions]
        print ("New Sequences: Mutation")
        for seq in newsequences:
            print(seq)        
        self.initsolution = newsequences

    def uniquentries(self, list):        
        for val in list:
            if not val in self.triedsolutions:
                self.triedsolutions.append(val)        

    def mutate(self, sequence, count=2):
        for i in range(count):
            j = random.randint(0, len(sequence)-1)
            k = random.randint(0, len(sequence)-1)
            sequence[j], sequence[k] = sequence[k], sequence[j]
            
        if random.uniform(0,1) < 0.25:
            j = random.randint(0, len(sequence)-1)
            k = random.randint(0, len(sequence)-1)
            sequence[j], sequence[k] = random.randint(1, self.n_queen), random.randint(1, self.n_queen)
        return sequence



    def cross(self, couple):
        list1 = couple[0]
        list2 = couple[1]
        randombreakpoint = random.randint(1, self.n_queen)
        newlist1 = list2[:randombreakpoint] + list1[randombreakpoint:]
        newlist2 = list1[:randombreakpoint] + list2[randombreakpoint:]
        templist = []
        templist.append(newlist1)
        templist.append(newlist2)
        return templist

    def getrandomcouples(self, returncount):
        cmblist = list(combinations(self.initsolution, 2))
        returnlist = []
        for i in range(int(returncount)):
            randvalue = random.randint(0, len(cmblist)-1)
            templist = []
            randvalue = random.randint(0, len(cmblist)-1)
            templist.append(cmblist[randvalue][0])
            randvalue = random.randint(0, len(cmblist)-1)
            templist.append(cmblist[randvalue][1])
            returnlist.append(templist)
        return returnlist

    def naturalselection(self):
        totalfitness = sum(self.fitnessscores)
        newfitnessscores = []
        newsolutions = []
        for i in range(len(self.initsolution)):
            if int(self.fitnessscores[i]) >= self.threshold:
                newfitnessscores.append(self.fitnessscores[i])
                newsolutions.append(self.initsolution[i])    
        self.initsolution = newsolutions
        self.fitnessscores = newfitnessscores
    
    def solutionfound(self):
        if self.maximumconflict in self.fitnessscores:
            return True
        return False

    def generateRandomSolution(self, n_primary):
        solution = []
        for i in range(n_primary):
            solution.append(self.randomsolution())
        return solution

    def randomsolution(self):
        return [random.randint(1, self.n_queen) for x in range(self.n_queen)]
    
    def showcurrentstate(self):
        print(self.initsolution)
    
    def getfitness(self):
        scorelist = []
        for solution in self.initsolution:
            scorelist.append(self.fitness(solution))
        return scorelist

    def fitness (self, arr):
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if math.fabs(arr[i] - arr[j]) == j - i or arr[i] == arr[j]:
                    count += 1
        return self.maximumconflict - count

    def ncr(self, n, r):
        return len(list(combinations([random.randint(1, n) for x in range(n)], r)))