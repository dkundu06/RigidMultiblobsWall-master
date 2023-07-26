'''
Write blobs configuration from location and orientation to visualize with Visit.

How to use:
python bodies_to_xyz.py input_file name_body_ID [output_name_body.config] 

with
input_file: the input file used to run the simulation.
name_body_ID: name of the rigid body to plot (i.e. active_dimer or passive_dimer).
output_name_body.config: the file generated by the main code with the configuration
                         of the rigid bodies with ID name_body_ID.
                         If not given the code will search it in the same folder as the input file.

Output:
output_name_body.xyz: blob configuration in xyz format.
                      The file will be saved in the same folder as the input file.
'''

import numpy as np
import argparse
import sys

sys.path.append('../')
sys.path.append('./')

import multi_bodies 
from quaternion_integrator.quaternion import Quaternion
from body import body 
from read_input import read_input
from read_input import read_vertex_file
from read_input import read_clones_file
from read_input import read_constraints_file
from read_input import read_vertex_file_list

if __name__ == '__main__':

  # Input files
  input_file = sys.argv[1]
  name_ID = sys.argv[2]
  if len(sys.argv) > 3:
    config_file = sys.argv[3]
  else:
    config_file = input_file[0:-9] + name_ID + '.config'

  # Output files
  name_output = config_file[:-6] + 'xyz'
  file_output = open(name_output, 'w')
  
  # Read input file
  read = read_input.ReadInput(input_file)
  a = read.blob_radius
  n_steps = read.n_steps
  n_save = read.n_save

  # Create rigid bodies
  bodies = []
  body_types = []
  num_blobs_ID = 0
  for ID, structure in enumerate(read.structures):
    # print 'Creating structures = ', structure[1] 
    struct_ref_config = read_vertex_file.read_vertex_file(structure[0]) 
    num_bodies_struct, struct_locations, struct_orientations = read_clones_file.read_clones_file(structure[1]) 
    body_types.append(num_bodies_struct) 
    # Creat each body of tyoe structure 
    for i in range(len(struct_orientations)): 
      b = body.Body(struct_locations[i], struct_orientations[i], struct_ref_config, a) 
      b.ID = read.structures_ID[ID] 
      # Append bodies to total bodies list 
      bodies.append(b) 
      if b.ID == name_ID:
        num_blobs_ID += b.Nblobs

  # Create articulated bodies
  for ID, structure in enumerate(read.articulated):
    # Read vertex, clones and constraint files
    struct_ref_config = read_vertex_file_list.read_vertex_file_list(structure[0], None)
    num_bodies_struct, struct_locations, struct_orientations = read_clones_file.read_clones_file(structure[1])
    constraints_info = read_constraints_file.read_constraints_file(structure[2], None)
    num_bodies_in_articulated = constraints_info[0]
    num_blobs = constraints_info[1]
    num_constraints = constraints_info[2]
    constraints_type = constraints_info[3]
    constraints_bodies = constraints_info[4]
    constraints_links = constraints_info[5]
    constraints_extra = constraints_info[6]

    # Read slip file if it exists
    body_types.append(num_bodies_struct)
    # body_names.append(read.articulated_ID[ID])
    # Create each body of type structure
    for i in range(num_bodies_struct):
      subbody = i % num_bodies_in_articulated
      first_blob  = np.sum(num_blobs[0:subbody], dtype=int)
      b = body.Body(struct_locations[i], struct_orientations[i], struct_ref_config[subbody], a)
      b.ID = read.articulated_ID[ID]
      # Append bodies to total bodies list 
      bodies.append(b) 
      if b.ID == name_ID:
        num_blobs_ID += b.Nblobs        
  bodies = np.array(bodies) 
  num_bodies = bodies.size 
  num_blobs = sum([x.Nblobs for x in bodies]) 

  # Read configuration 
  with open(config_file, 'r') as f: 
    for step in range(n_steps // n_save + 1): 
      # Read bodies
      data = f.readline()
      if data == '' or data.isspace():
        break

      file_output.write(str(num_blobs_ID) + '\n#\n')
      for k, b in enumerate(bodies):
        if b.ID == name_ID:
          data = f.readline().split()
          b.location = [float(data[0]), float(data[1]), float(data[2])]
          b.orientation = Quaternion([float(data[3]), float(data[4]), float(data[5]), float(data[6])])
          for ri in b.get_r_vectors():
            file_output.write(b.ID[0].upper() + ' %s %s %s \n' % (ri[0], ri[1], ri[2]))


