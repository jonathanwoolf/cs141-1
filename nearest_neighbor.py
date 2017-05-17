import sys
from math import sqrt
import re
import random
import time

pointRE=re.compile("(-?\\d+.?\\d*)\\s(-?\\d+.?\\d*)")

def dist(p1, p2):
	return sqrt(pow(p1[0]-p2[0],2) + pow(p1[1]-p2[1],2))

#Run the divide-and-conquor nearest neighbor 
def nearest_neighbor(points):
	if (len(points) <= 3): return brute_force_nearest_neighbor(points)
	else: 
		ordered = sorted(points) 
		#middle = len(ordered)/2
		#orderedL = ordered[:middle]
		#orderedR = ordered[middle:] 
		return nearest_neighbor_recursion(ordered)

#Brute force version of the nearest neighbor algorithm, O(n**2)
def brute_force_nearest_neighbor(points):
	if (len(points) < 2): return 100000 #checks for array size less than 2
	min_distance = dist(points[0], points[1]) #sets min_distance
	for i in range (0, (len(points) - 1)): 
		for j in range ((i + 1), (len(points) - 1)):
			if (dist(points[i], points[j]) < min_distance): 
				min_distance = dist(points[i], points[j]) #sets min_distance to lower distance
	return min_distance

def nearest_neighbor_recursion(ordered):
	if (len(ordered) <= 3): return brute_force_nearest_neighbor(ordered) #checks for array size less than 3
	
	middle = int(len(ordered)/2)
	orderedL = ordered[:middle]
	orderedR = ordered[middle:]
	DL = nearest_neighbor_recursion(orderedL)
	DR = nearest_neighbor_recursion(orderedR)
	min_distance = min(DL, DR)
	
	XL = ordered[middle][0] - DL 
	XR = ordered[middle][0] + DR 
	while(ordered[0][0] < XL): 
		ordered.remove(ordered[0])
	while(ordered[-1][0] > XR): 
		ordered.remove(ordered[-1]) 
	pin_points = ordered
	
	min_distance_pin = brute_force_nearest_neighbor(pin_points)
	if min_distance < min_distance_pin:
		return min_distance
	else: return min_distance_pin

def read_file(filename):
    points=[]
    # File format
    # x1 y1
    # x2 y2
    # ...
    in_file=open(filename,'r')
    for line in in_file.readlines():
        line = line.strip()
        point_match=pointRE.match(line)
        if point_match:
        	x = float(point_match.group(1))
        	y = float(point_match.group(2))
        	points.append((x,y))
    #print(points)
    return points

def main(filename,algorithm):
	algorithm=algorithm[1:]
	points=read_file(filename)
	
	#Create output file
	outputfile = filename[0:-4] + "_distance.txt"

	if algorithm =='dc':
		start_time = time.time()
		divide = nearest_neighbor(points) 
		end_time = time.time()
		total_time = end_time - start_time
		f = open(outputfile, 'w')
		f.write(str(divide) + "\n")
		f.close()
		print("Divide and Conquer: " +  str(divide))
		print("Run Time: " + str(total_time)) 
	if algorithm == 'bf':
		start_time = time.time()
		brute = brute_force_nearest_neighbor(points)
		end_time = time.time()
		total_time = end_time - start_time 
		f = open(outputfile,'w') 
		f.write(str(brute) + "\n") 
		f.close()
		print("Brute Force: " + str(brute))
		print("Run Time: " + str(total_time))
	if algorithm == 'both':
		start_time = time.time() 
		divide = nearest_neighbor(points)
		end_time = time.time()
		total_time = end_time - start_time
		f = open(outputfile, 'w')
		f.write(str(divide) + "\n") 
		f.close()
		print("Divide and Conquer: " +  str(divide))
		print("Run Time: " + str(total_time)) 
		start_time = time.time()
		brute = brute_force_nearest_neighbor(points) 
		end_time = time.time()
		total_time = end_time - start_time
		print("Brute Force: " + str(brute))
		print("Runt Time: " + str(total_time)) 

if __name__ == '__main__':
    	if len(sys.argv) < 3:
        	print("python assignment1.py -<dc|bf|both> <input_file>")
        	quit(1)
    	if len(sys.argv[1]) < 2:
        	print("python assignment1.py -<dc|bf|both> <input_file>")
        	quit(1)
    	main(sys.argv[2],sys.argv[1])
