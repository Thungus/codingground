import numbers_v2, time, ChrisNumbers

testNum = 999
testIterations = 1000000

conlinSum = 0
chrisSum = 0

print('Conlin:\t',numbers_v2.numeralsToWords(testNum))
print('Chris:\t',ChrisNumbers.numberToWords(testNum))

for i in range(0,testIterations):
	starttime = time.clock()
	numbers_v2.numeralsToWords(testNum)
	endtime = time.clock()
	conlinSum += (endtime-starttime)

print("Conlin:\t", conlinSum / testIterations)

chrisList = []
for i in range(0,testIterations):
	starttime = time.clock()
	ChrisNumbers.numberToWords(testNum)
	endtime = time.clock()
	chrisSum += (endtime-starttime)

print("Chris:\t", chrisSum / testIterations)