import matplotlib
matplotlib.use('Agg') # no UI backend

import numpy as np
import matplotlib.pyplot as plt
import random

theoreticalValue = 0.857
numberOfTries = 10000

analizedKey = "2"

graph = {
        "1" : ["2", "4"], 
        "2" : ["1", "3"],
        "3" : ["3"],
        "4" : ["1", "3", "5"],
        "5" : ["5"]}




numVisitations = []
averageTries = []

for experimentCnt in range(numberOfTries):
    flyPos = "1"
    visitationCnt = 0
    # Grafo está na aranha ou na janela,
    while((flyPos != "3") and (flyPos != "5")):
        # A mosca anda aleatoriamente para algum nó ligado
        flyPos = random.choice(graph[flyPos])
        if(flyPos == analizedKey):
            visitationCnt += 1
        

    numVisitations.append(visitationCnt)
    averageTries.append(sum(numVisitations)/len(numVisitations))
    

plt.figure(figsize=(8,6))
plt.axhline(y = theoreticalValue, linestyle='-', color='red', linewidth=2, label = 'Theoretical Value'+ ": (" + str(theoreticalValue) + ")")
plt.plot(range(len(averageTries)),averageTries, linestyle='-', color='blue', linewidth=2, label = 'Simulated Value')
plt.xlabel("nº of Experiments", fontsize=20)
plt.ylabel("Average nº of visitation in " + analizedKey, fontsize=20)
plt.legend()
plt.grid(True)
plt.savefig("exercise1b-"+analizedKey+".png")  #savefig, don't show

    
        



