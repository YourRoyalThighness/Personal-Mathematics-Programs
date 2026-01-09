m = 1
sumList = []
finSum = 0 
for m in range(1,21):
    numAdd = input((27 + (37/2) * m)**2)
    sumList.append(numAdd)
for i in range(len(sumList)):
    finSum = finSum + sumList[i]
print(finSum)