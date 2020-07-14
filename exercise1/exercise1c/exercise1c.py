import matplotlib
matplotlib.use('Agg') # no UI backend

import numpy as np
import matplotlib.pyplot as plt
import random

theoreticalValue = 12
numberOfExperiments = 50000

graph = {
        "1" : ["2", "4"], 
        "2" : ["1", "3"],
        "3" : ["4", "2"],
        "4" : ["1", "3", "5"],
        "5" : ["5"]}


numSteps = []
averageSteps = []

for experimentCnt in range(numberOfExperiments):
    flyPos = "1"
    stepCnt = 0
    # Grafo está na aranha ou na janela,
    while((flyPos != "5")):
        # A mosca anda aleatoriamente para algum nó ligado
        flyPos = random.choice(graph[flyPos])
        stepCnt += 1
        

    numSteps.append(stepCnt)
    averageSteps.append(sum(numSteps)/len(numSteps))
    

plt.figure(figsize=(8,6))
plt.axhline(y = theoreticalValue, linestyle='-', color='red', linewidth=2, label = 'Theoretical Value'+ ": (" + str(theoreticalValue) + ")")
plt.plot(range(len(averageSteps)),averageSteps, linestyle='-', color='blue', linewidth=2, label = 'Simulated Value')
plt.xlabel("nº of Experiments", fontsize=20)
plt.ylabel("Average nº of Steps to window", fontsize=20)
plt.legend()
plt.grid(True)
plt.savefig("exercise1c.png")  #savefig, don't show

    
        



