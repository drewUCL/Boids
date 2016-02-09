from matplotlib import pyplot as plt
from matplotlib import animation
import random

# --------------- To move into file (e.g YAML) ---------------
boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
# ---------------------------- End ----------------------------

#NOTE: I need to code in 'self.' to this class -- this will be done after I figure out the __init__ and think through the logic of methods of moving the flock in certain directions etc 

class BoidsMethod(object):
	''' 
	Description: A class to encase the Boids simulation mathods using object orientation design
	'''
	
	def __init__(self, positions, velocities, fields):
		self.positions = positions #To code an implementation to initiate flocks
		self.velocities = velocities #To code an implementation to initiate flocks
		self.fields = fields #Passed as an array of method calls (methods will be coded in this class)
	
	def update_boids(self, boids):
		xs,ys,xvs,yvs=boids
		# Fly towards the middle
		for i in range(len(xs)):
			for j in range(len(xs)):
				xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
		for i in range(len(xs)):
			for j in range(len(xs)):
				yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
		# Fly away from nearby boids
		for i in range(len(xs)):
			for j in range(len(xs)):
				if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
					xvs[i]=xvs[i]+(xs[i]-xs[j])
					yvs[i]=yvs[i]+(ys[i]-ys[j])
		# Try to match speed with nearby boids
		for i in range(len(xs)):
			for j in range(len(xs)):
				if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
					xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
					yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
		# Move according to velocities
		for i in range(len(xs)):
			xs[i]=xs[i]+xvs[i]
			ys[i]=ys[i]+yvs[i]


	def animate(self, frame):
	   update_boids(boids)
	   scatter.set_offsets(zip(boids[0],boids[1]))


	def deploy_simulation(self):
		figure=plt.figure()
		axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
		scatter=axes.scatter(boids[0],boids[1])
		anim = animation.FuncAnimation(figure, animate,frames=50, interval=50)

if __name__ == "__main__":
	obj_boid = BoidsMethod()
    obj_boid.deploy_simulation()
