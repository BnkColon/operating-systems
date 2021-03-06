# Bianca I. Colon Rosado
# $ python fifo.py input.txt	

from string import *
from sys import argv

if (len(argv) == 2):		# If recive $ python fifo.py input.txt
	fileInput = argv[1] 	# Save the file input gived in the command line
							# print type(fileInput) / <type 'str'>
else:						# If not recieve this $ python fifo.py input.txt
		fileInput = 'input.txt'	# Search for a file named input.txt [10,2,3,4]
f = open(fileInput)		# Open the file in read mode
						# print f / <open file 'input.txt', mode 'r' at 0x2b366f908e40>
lists = f.readlines()	# Read all the file
f.close()				# Close the file
processes = []			# Empty list for the processes

totalnum = 0 			# Initialize variable
average = 0 			# Initialize variable

for i in range(len(lists)):		# Go througth the list
	processes.append(int(lists[i].rstrip()))	# Append int values in processes list
	totalnum += processes[i] 	# Increment with the processes
	average += totalnum 		# Sum the final values to calculate the average
	print 'P%s:%d' % (i+1, totalnum) 	# Print process ID : Time spended

average = float(average) / len(lists)	# Calculate the average
print 'Avg:%1.1f' % (average)	# Print Avg : float final number with 1 decimal space