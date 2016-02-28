from matplotlib import pyplot as plt
from matplotlib import animation

import os
import yaml
import numpy as np


class BoidsMethod(object):
	'''
	Description: A class to allow execution of boids methods 
	'''
	
	def __init__( self,
	              position_bounds = [-450.0, 300.0, 50.0, 600.0],
	              velocity_bounds = [0.0, -20.0, 10.0, 20.0],
	              count = 50,
	              frames = 50,
	              interval = 50,
	              xlim = (-500,1500),
	              ylim = (-500,1500),
	              threshold = 10000, # Threshold for matching speeds
	              must_fly_away = 100, # Threshold for flying away from nearby boids
	              speed_with_nearby_boids_calibration = 0.125,
	              fly_to_middle_gravity = 0.01 ):
		''' The init has been provided with default values to overload by the config file from the command line interface. If the command load did not work the user will have the option to simply use the defaults '''
		
		self.velocity_bounds = velocity_bounds 
		self.position_bounds = position_bounds
		
		self.count = count
		self.frames = frames
		self.interval = interval
		self.xlim = xlim
		self.ylim = ylim
		
		self.threshold = threshold
		self.must_fly_away = must_fly_away
		self.speed_with_nearby_boids_calibration = speed_with_nearby_boids_calibration
		self.fly_to_middle_gravity = fly_to_middle_gravity
		
		self.positions  = self.generate_boids_flock( np.array(self.position_bounds[0:2]),
		                                             np.array(self.position_bounds[2:4]) )
		self.velocities = self.generate_boids_flock( np.array(self.velocity_bounds[0:2]),
		                                             np.array(self.velocity_bounds[2:4]) )
		
	def move_according_to_velocities(self):
		self.positions += self.velocities
	
	def try_to_match_speed_with_nearby_boids(self):
		position_difference = self.find_differences(self.positions)
		velocity_difference = self.find_differences(self.velocities)
		distances = self.compute_limit(position_difference, self.threshold)
		reset_velocity_position_rule = self.limit_descisions(velocity_difference, distances)
		self.velocities -= np.mean( reset_velocity_position_rule,1 ) * \
		                            self.speed_with_nearby_boids_calibration
		
	def limit_descisions(self, differences, distance):
		differences[0,:,:][distance] = 0 
		differences[1,:,:][distance] = 0
		return differences
	
	def compute_limit(self, differences, threshold_value):
		square_error = differences**2
		sum_square_error = np.sum(square_error,0)
		return sum_square_error > threshold_value
	
	def find_differences(self, positions):
		difference = positions[:,np.newaxis,:] - \
		             positions[:,:,np.newaxis]
		return difference 
		
	def fly_away_from_nearby_boids(self):
		differences = self.find_differences(self.positions)
		distance = self.compute_limit(differences, self.must_fly_away)
		seperation_rules = self.limit_descisions(differences, distance)
		self.velocities += np.sum(seperation_rules,1)
	
	def fly_towards_middle(self):
		center = np.mean(self.positions,1)
		find_direction_to_travel = self.positions - center[:,np.newaxis]
		self.velocities -= find_direction_to_travel * \
		                   self.fly_to_middle_gravity
	
	def generate_boids_flock(self, lower_bound, upper_bound):
		width = abs(lower_bound - upper_bound)
		return (lower_bound[:, np.newaxis] + np.random.rand(2, self.count) \
		        * width[:, np.newaxis])
	
	def delploy_simulation(self):
		figure = plt.figure()
		axes = plt.axes(xlim=self.xlim, ylim=self.ylim)
		self.scatter = axes.scatter(self.positions[0],self.positions[1])
		anim = animation.FuncAnimation( figure, self.animate,
	                                    frames = self.frames,
	                                    interval = self.interval )
		plt.show()

	def animate(self, frame):
	   self.update_boids()
	   self.scatter.set_offsets(self.positions.transpose())
	
	def update_boids(self):	
		self.fly_towards_middle() # Fly towards the middle
		self.fly_away_from_nearby_boids() # Fly away from nearby boids
		self.try_to_match_speed_with_nearby_boids() # Try to match speed with nearby boids
		self.move_according_to_velocities() # Move according to velocities

if __name__ == "__main__": 
	# This has been left here to allow testing of this file
	boid_object = BoidsMethod()
	boid_object.delploy_simulation()
	

	
	
	
	
	