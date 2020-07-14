import matplotlib
matplotlib.use('Agg') # no UI backend

import numpy as np
import matplotlib.pyplot as plt
import random

colors = ['#ff0000', '#050dff', '#00ff26', '#ff6a00', '#ee00ff']
theoreticalColors = ['#fa5c5c','#6b70ff','#75bd7f', '#ffa15e', '#f785ff']
theoreticalValue = [0.1875, 0.09375, 0.1875, 0.15625, 0.375]
numberOfExperiments =  1000
numberOfSteps = 1000

#each connection is composed of [0]-> node connected, [1]-> weight, [2]-> probability
graph = {
            "1" : [["2", 3, 0], ["4", 1, 0], ["5", 2, 0]], 
            "2" : [["1", 3, 0]],
            "3" : [["5", 6, 0]],
            "4" : [["1", 1, 0], ["5", 4, 0]],
            "5" : [["1", 2, 0], ["3", 6, 0], ["4", 4, 0]]
        }

for node in graph:
    sumWeigths = 0
    for connection in graph[node]:
        sumWeigths += connection[1]
    for connection in graph[node]:
        connection[2] = connection[1]/sumWeigths
    
visitationCnt = [0,0,0,0,0]
numVisitations = [[], [], [], [], []]
averageVisitations = [[],[],[],[],[]]


for experimentCnt in range(numberOfExperiments):
    currentPos = "1"
    visitationCnt = [0,0,0,0,0]
    for stepCnt in range(numberOfSteps): 
        #conta a visita atual
        visitationCnt[int(currentPos) - 1] += 1

        #Gera um numéro aleátorio é faz o passo a depender do número gerado
        randStep = np.random.uniform() 
        lastProbBuffer = 0
        for connection in graph[currentPos]:
            #Checa o intervalo da probabilidade
            if(lastProbBuffer <= randStep and randStep < lastProbBuffer + connection[2] ):
                currentPos = connection[0]
                break
                
            lastProbBuffer += connection[2]
    
    #Registra as contagens
    for index in range(len(graph)):
        numVisitations[index].append(visitationCnt[index]/numberOfSteps)
        averageVisitations[index].append(sum(numVisitations[index])/len(numVisitations[index]))



    

plt.figure(figsize=(8,6))

#plota o gráfico
for i in  range(len(graph)):
    plt.axhline(y = theoreticalValue[i], linestyle='-', color=theoreticalColors[i], linewidth=2, label = 'Theoretical Value ' + str(i) + ": (" + str(theoreticalValue[i]) + ")")
    plt.plot(range(len(averageVisitations[i])),averageVisitations[i], linestyle='-', color=colors[i], linewidth=2, label = 'Simulated Value ' + str(i))
   

plt.xlabel("nº of Experiments", fontsize=20)
plt.ylabel("Average (nº of visitation / Total steps)", fontsize=20)
plt.legend()
plt.grid(True)
plt.savefig("exercise4.png")  #savefig, don't show

    
        