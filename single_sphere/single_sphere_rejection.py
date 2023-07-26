'''This script will display a histogram of a single sphere's height when next to a wall using sphere.py.
1,000,000 heights will be generated by iterating over n_steps, and written to a text file: rejection_locations.txt
On top of the histogram is a plot of the analytical GB distribution  
Prints the time taken for all the calculations'''


import numpy as np
import time
import sphere as s

outFile = 'rejection_locations.txt'
# constants listed for convenience, none here are changed from what is in sphere.py
s.A = 0.265*np.sqrt(3./2.)
s.VISCOSITY = 8.9e-4
s.WEIGHT = 1.*0.0000000002*(9.8*1e6)
s.KT = 300.*1.3806488e-5
s.REPULSION_STRENGTH = 7.5 * s.KT
s.DEBYE_LENGTH = 0.5*s.A

sample_state = [0., 0., 1.1] # the position of a single sphere
n_steps = 1000000 # the number of height positions to be generated
f = open(outFile, 'w')

start_time = time.time() 

# generate appropriate normalization constant
partition_steps = 10000 # number of samples generated for Z
partitionZ = s.generate_partition(partition_steps)

for i in range(n_steps):
	# get a position from rejection function
	sample_state = s.single_sphere_rejection(partitionZ)
	# send that position to the data file
	f.write(str(sample_state[2]) + '\n')
f.close()

end_time = time.time() - start_time
print(end_time) # should take somewhere around 80 seconds for one million heights

num_points = 100000
x, y = s.analytical_distribution(num_points) # calculate points for the analytical curve

s.plot_distribution(outFile, x, y, n_steps) # generate historgram and analytical curve