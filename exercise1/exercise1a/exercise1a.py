import matplotlib
matplotlib.use('Agg') # no UI backend

import numpy as np
import matplotlib.pyplot as plt
import random

theoreticalValue = 0.286
numberOfExperiments = 50000

graph = {
        "1" : ["2", "4"], 
        "2" : ["1", "3"],
        "3" : ["3"],
        "4" : ["1", "3", "5"],
        "5" : ["5"]}

winCnt = 0

probabilities = []

for experimentCnt in range(numberOfExperiments):
    flyPos = "1"

    # Grafo está na aranha ou na janela,
    while((flyPos != "5" and flyPos != "3")):
        # A mosca anda aleatoriamente para algum nó ligado
        flyPos = random.choice(graph[flyPos])
        
    if(flyPos == "5"):
        winCnt += 1


    probabilities.append(winCnt/(experimentCnt+1)) 
    
    

plt.figure(figsize=(8,6))
plt.axhline(y = theoreticalValue, linestyle='-', color='red', linewidth=2, label = 'Theoretical Value'+ ": (" + str(theoreticalValue) + ")")
plt.plot(range(len(probabilities)),probabilities, linestyle='-', color='blue', linewidth=2, label = 'Simulated Value')
plt.xlabel("nº of Experiments", fontsize=20)
plt.ylabel("probability", fontsize=20)
plt.legend()
plt.grid(True)
plt.savefig("exercise1a.png")  #savefig, don't show

    
        
