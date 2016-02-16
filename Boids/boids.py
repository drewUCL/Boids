from matplotlib import pyplot as plt
from matplotlib import animation

import os
import yaml
import numpy as np


'''

TODO: 
	REFACTOR THE INNER WORKINGS OF:
		1. move_according_to_velocities
		2. try_to_match_speed_with_nearby_boids
		3. fly_away_from_nearby_boids
		4. fly_towards_middle

'''

class BoidsMethod(object):
	def __init__(self, position_bounds, velocity_bounds):
		
		self.velocity_bounds = velocity_bounds 
		self.position_bounds = position_bounds
		
		self.count = 50
		self.frames = 50
		self.interval = 50
		self.xlim = (-500,1500)
		self.ylim = (-500,1500)
		
		self.positions  = self.generate_boids_flock( np.array(self.position_bounds[0:2]),np.array(self.position_bounds[2:4]) )
		self.velocities = self.generate_boids_flock( np.array(self.velocity_bounds[0:2]),np.array(self.velocity_bounds[2:4]) )
		
		#Encapsulate into a discionary for readability
		self.update = {'X Position': self.positions[0], 'Y Position':self.positions[1], 'X Velocity': self.velocities[0],'Y Velocity':self.velocities[1]}

	def delploy_simulation(self):
		figure = plt.figure()
		axes = plt.axes(xlim=self.xlim, ylim=self.ylim)
		self.scatter = axes.scatter(self.positions[0],self.positions[1])
		anim = animation.FuncAnimation(figure, self.animate, frames = self.frames, interval = self.interval)
		plt.show()

	def animate(self, frame):
	   self.update_boids() #self.positions, self.velocities
	   self.scatter.set_offsets(self.positions.transpose())
	   
	def generate_boids_flock(self, lower_limits, upper_limits):
		width = abs(upper_limits - lower_limits)
		return (lower_limits[:, np.newaxis] + np.random.rand(2, self.count) * width[:, np.newaxis])
	   

	def update_boids(self):	
		self.fly_towards_middle() # Fly towards the middle
		self.fly_away_from_nearby_boids() # Fly away from nearby boids
		self.try_to_match_speed_with_nearby_boids() # Try to match speed with nearby boids
		self.move_according_to_velocities() # Move according to velocities
	
	def move_according_to_velocities(self):
		for i in range(len(self.update['X Position'])):
			self.update['X Position'][i]=self.update['X Position'][i]+self.update['X Velocity'][i]
			self.update['Y Position'][i]=self.update['Y Position'][i]+self.update['Y Velocity'][i]
	
	def try_to_match_speed_with_nearby_boids(self):
		for i in range(len(self.update['X Position'])):
			for j in range(len(self.update['X Position'])):
				if (self.update['X Position'][j]-self.update['X Position'][i])**2 + (self.update['Y Position'][j]-self.update['Y Position'][i])**2 < 10000:
					self.update['X Velocity'][i]=self.update['X Velocity'][i]+(self.update['X Velocity'][j]-self.update['X Velocity'][i])*0.125/len(self.update['X Position'])
					self.update['Y Velocity'][i]=self.update['Y Velocity'][i]+(self.update['Y Velocity'][j]-self.update['Y Velocity'][i])*0.125/len(self.update['X Position'])
	
	def fly_away_from_nearby_boids(self):
		for i in range(len(self.update['X Position'])):
			for j in range(len(self.update['X Position'])):
				if (self.update['X Position'][j]-self.update['X Position'][i])**2 + (self.update['Y Position'][j]-self.update['Y Position'][i])**2 < 100:
					self.update['X Velocity'][i]=self.update['X Velocity'][i]+(self.update['X Position'][i]-self.update['X Position'][j])
					self.update['Y Velocity'][i]=self.update['Y Velocity'][i]+(self.update['Y Position'][i]-self.update['Y Position'][j])
	
	def fly_towards_middle(self):
		for i in range(len(self.update['X Position'])):
			for j in range(len(self.update['X Position'])):
				self.update['X Velocity'][i]=self.update['X Velocity'][i]+(self.update['X Position'][j]-self.update['X Position'][i])*0.01/len(self.update['X Position'])
		for i in range(len(self.update['X Position'])):
			for j in range(len(self.update['X Position'])):
				self.update['Y Velocity'][i]=self.update['Y Velocity'][i]+(self.update['Y Position'][j]-self.update['Y Position'][i])*0.01/len(self.update['X Position'])

if __name__ == "__main__":
	# load factors from yaml file
	
	with open(os.path.join(os.path.dirname(__file__),'factors','factors.yaml')) as factor_data:
		test_data = yaml.load(factor_data)['factors']
		for point in test_data:
			position_bounds = point.pop('position_bounds')
			velocity_bounds = point.pop('velocity_bounds')
	
	boid_object = BoidsMethod( position_bounds, velocity_bounds )
	boid_object.delploy_simulation()
	

	
	
	
	
	