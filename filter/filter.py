import queue

MAX_VALUES_IN_QUEUE = 100

class Filter:
	def __init__(self):
		self.q = queue.Queue(MAX_VALUES_IN_QUEUE)

	def put(self, Val):
		self.q.put(Val)
		
	def avg_of_array(self, A):
		'''classical average'''
		avg = 0
		length = len(A)
		for i in range(length):
			avg += A[i]

		return avg/length

	def decay_avg_of_array(A):
		'''older values have less impact on the average'''
		avg = 0
		length = len(A)
		for i in range(length):
			avg += A[i] * (length - i)/length
			
		return avg/length

	def classify(self, val, maximum, nr_of_classes):
		classes = (maximum/nr_of_classes)
		for i in range(nr_of_classes + 1):
			if (val <= i * classes):
				return i 
		
		return (nr_of_classes, val)

	def latest_class(self, nr_of_values):
		if(self.q.qsize() < nr_of_values):
			return

		A = []
		for i in range(nr_of_values):
			A.append(self.q.get())

		return self.classify(self.avg_of_array(A), 100, 4)

	def size(self):
		self.q.qsize()

