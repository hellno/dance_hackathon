import Queue
from random import random

MAX_VALUES_IN_QUEUE = 100

q = Queue.Queue(MAX_VALUES_IN_QUEUE)

def avg_of_array(A):
	avg = 0
	length = len(A)
	for i in range(length):
		avg += A[i]

	return avg/length

def classify(val, maximum, nr_of_classes):
	classes = (maximum/nr_of_classes)
	for i in range(nr_of_classes + 1):
		if (val <= i * classes):
			return i 

for i in range(21):
	q.put(random()*100)

print "%d (!= 21) elements in queue" % q.qsize()

while q.qsize() > 5:
	A = []
	
	for i in range(5):
		A.append(q.get())

	avg = avg_of_array(A)
	
	print "Avg of array %f in class" % avg, classify(avg, 100, 100)

print "%d remaining elements in queue" % q.qsize()
