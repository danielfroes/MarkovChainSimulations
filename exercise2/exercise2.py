import matplotlib
matplotlib.use('Agg') # no UI backend
import numpy as np
import matplotlib.pyplot as plt

theoreticalValue = 0.3
maxValue = 1
winProb = 0.49
numberOfTries = 100000
winCnt = 0
probabilities = []

for tryCnt in range(numberOfTries):
    currentValue = 6
    # Se perder ou ganhar
    while((currentValue > 0) and (currentValue < maxValue)):
        if(np.random.uniform() < winProb):
            currentValue += 1
        else:
            currentValue -= 1
    # Ganhou
    if(currentValue >= maxValue):
        winCnt += 1
        
    probabilities.append(winCnt/(tryCnt+1)) 


plt.figure(figsize=(8,6))
plt.axhline(y = theoreticalValue, linestyle='-', color='red', linewidth=2, label = 'Theoretical Value'+ ": (" + str(theoreticalValue) + ")")
plt.plot(range(len(probabilities)),probabilities, linestyle='-', color='blue', linewidth=2, label = 'Simulated Value')
plt.xlabel("nº of Tries", fontsize=20)
plt.ylabel("Probability", fontsize=20)
plt.legend()
plt.grid(True)
plt.savefig("exercise2.png")  #savefig, don't show

    
        
