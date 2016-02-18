import json
import ConfigParser 

import traceback
import logging
import datetime 
import sys

from matplotlib import pyplot as plt
from argparse import ArgumentParser
from boids import BoidsMethod

'''
TODO:
	1. Create configeration file - DONE
	2. Link configs - DONE
	3. Exception handling - add firther IOError etc etc

'''

def user_run_defaults():
	user_input = raw_input('would you like to run with default values? [y/n]')
	if(user_input == 'Y' or user_input == 'y'):
		boid_object = BoidsMethod()
		boid_object.delploy_simulation()
	else:
		print '## You did not run the Boids programme with the default file'
		print '## Exiting programme'
		sys.exit()

def command():
	''' 
	Description: A function to communicate with the command line. This function is linked with the setup.py file.
	'''
	
	parser = ArgumentParser(prog="Boids", description = "The Boids Flocking Bird Simulation")
	parser.add_argument('--config','-c',help='Please select a config file',default='config.cfg')
	args = parser.parse_args()
	
	
	try : 
		configuration = ConfigParser.ConfigParser()
		with open(os.path.join(os.path.dirname(__file__),'factors',args.config)) as c:
			configuration.readfp(c)
			
			#use data specific getters and setters, e.g getint for int and getfloat for float. First argument is in the [] within the config file is the section of the data
			
			#Load boids main data [Boids]
			count = configuration.getint('Boids','count')
			frames = configuration.getint('Boids','frames')
			interval = configuration.getint('Boids','interval')
			position_bounds = configuration.get('Boids','position_bounds')
			velocity_bounds = configuration.get('Boids','velocity_bounds')
			
			#Load axis data [Axis_limits]
			xlim = configeration.get('Axis_limits','xlim')
			ylim = configeration.get('Axis_limits','ylim')
			
			# Load flock dynamics [Flock_Dynamics]
			threshold = configuration.getint('Flock_Dynamics','threshold')
			must_fly_away = configuration.getint('Flock_Dynamics','must_fly_away')
			speed_with_nearby_boids_calibration = configuration.getfloat('Flock_Dynamics','speed_with_nearby_boids_calibration')
			fly_to_middle_gravity = configuration.getfloat('Flock_Dynamics','fly_to_middle_gravity')
			
		## Now load the parameters into the BoidMethod
		boid_object = BoidsMethod( 
					position_bounds, 
					velocity_bounds,
					count,
					frames,
					interval,
					xlim,
					ylim,
					threshold,
					must_fly_away,
					speed_with_nearby_boids_calibration,
					fly_to_middle_gravity
					)
		boid_object.delploy_simulation()
		
	except IOError as e:
		''' Catch this IO error (very specific error handling) '''
		print '## Your config file did not load'
		user_run_defaults()
			
	except Exception as e:
		''' Catch more general errors and show a traceback allowing an easy debug '''
		tracker = datetime.now()
		print("THERE HAS BEEN AN ERROR WITH LOADING THE CONFIGURATIONS INTO THIS PROGRAMME AT %s" % datetime.strptime(tracker, "%d/%m/%y %H:%M"))
		logging.error(traceback.format_exc())