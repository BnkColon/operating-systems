# Bianca I. Colon Rosado
# $ python rr.py quanta input.txt	
from string import *
from sys import argv


class Process:
	"""docstring for Process"""
	def __init__(self, pid, ptime):
		self.id = pid			# Take the ID of that instance
		self.time = int(ptime)	# Take the time of that instance
		self.qConsumption = 0 	# Initialize the consumption time to 0
	def __str__(self):			# Return the string version of the instance
		return str(self.id) + str(self.qConsumption)

	def setTime(self, ptime):	# Set the time 
		self.time = ptime

	def getTime(self):			# Return the time 
		return self.time

	def getID(self):			# Return the ID 
		return self.id

	def setQuanta(self, qConsumption):	# Set the Quanta 
		self.qConsumption = qConsumption

	def getQuanta(self):		# Return the Quanta 
		return self.qConsumption


def main():

	if (len(argv) == 3):		# If recive $ python rr.py quanta input.txt
		quanta = int(argv[1])	# Save the quanta number gived in the command line
								# print type(quanta)		/ <type 'int'>
		fileInput = argv[2] 	# Save the file input gived in the command line
								# print type(fileInput) 	/ <type 'str'>
	else:						# If not recieve this $ python rr.py quanta input.txt
		quanta = 3				# Assing quanta = 3
		fileInput = 'input.txt'	# Search for a file named input.txt [10,2,3,4]

	f = open(fileInput)		# Open the file in read mode
							# print f / <open file 'input.txt', mode 'r' at 0x2b366f908e40>
	lists = f.readlines()	# Read all the file


	f.close()				# Close the file

	results = [None] * len(lists)	# Create a empty list with the maxsize of the processes 
	
	for i in range(len(lists)):		# Iterate throught lists, to create the processes (instances)
		lists[i] = Process(i, int(lists[i].strip()))	# Process('P'+str(i+i)+':')

	quantaTotal = 0 		# Variable "Global" to get the quantum time of all processes
	average = 0 			# Variable that save the average of all the processes
	while lists: 			# While lists is not empty
		finished_processes = []	# Empty list to save the index of the processes that finished
		for i in range(len(lists)):	# Iterate all processes
			if (lists[i].getTime() <= quanta): 	# If the time of the process is minor or equal to the quantum
				if (lists[i].getTime() == quanta):	# If is equal to the quantum
					quantaTotal += quanta 		# Save the quantum
				else:		# If the time of the process is minor to the quantum
					quantaTotal += lists[i].getTime() 	# Save time of the process
				lists[i].setQuanta(quantaTotal)	# Set the quantum to the process
				lists[i].setTime(0)				# When finished set the time to 0
				results[lists[i].getID()] = lists[i] 	# Insert the index to remove
				finished_processes.insert(0, i)	# Insert to the list of finished processes
				#print i, lists[i].getQuanta()
			else:			# If the time of the process is bigger to the quantum
				lists[i].setTime(int(lists[i].getTime()) - quanta) # To the time rest quanta
				quantaTotal += quanta 			# Save the quantum
				lists[i].setQuanta(quantaTotal) # Set the quantum to the process
				# print i, lists[i].getQuanta()
		
		for i in finished_processes:	# Iterate the list of finished processes
			lists.pop(i)	# Delete from the list of processes 
	# Close While
	for i in range(len(results)):		# Iterate the list of results
		print 'P%d:%d' %(results[i].getID() + 1,results[i].getQuanta()) # Print P(ID):Time spended
		average += results[i].getQuanta() # Save all the time spended
	average = float(average)/ len(results) # to calculate the average
	print 'Avg:%1.2f' % (average)		# print Average


if __name__ == '__main__':
	main()











