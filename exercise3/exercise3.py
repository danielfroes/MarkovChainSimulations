import matplotlib
matplotlib.use('Agg') # no UI backend


import numpy as np
import matplotlib.pyplot as plt

theoreticalValue = 6

headProb = 0.5

numberOfTries = 100000



winCnt = 0

triesArray = []
averageTries = []
for experimentCnt in range(numberOfTries):
    
    headCnt = 0 
    numberOfTries = 0 

    # Se perder ou ganhar
    while(headCnt < 2):
        numberOfTries += 1
        if(np.random.uniform() <= headProb):
            headCnt += 1
        else:
            headCnt = 0
    
    triesArray.append(numberOfTries)
    averageTries.append(sum(triesArray)/len(triesArray))


plt.figure(figsize=(8,6))
plt.axhline(y = theoreticalValue, linestyle='-', color='red', linewidth=2, label = 'Theoretical Value'+ ": (" + str(theoreticalValue) + ")")
plt.plot(range(len(averageTries)),averageTries, linestyle='-', color='blue', linewidth=2, label = 'Simulated Value')
plt.xlabel("nº of experiments", fontsize=20)
plt.ylabel("Average of tries", fontsize=20)
plt.legend()
plt.grid(True)
plt.savefig("exercise3.png")  #savefig, don't show

    
        
