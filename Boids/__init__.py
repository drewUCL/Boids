import json
import ConfigParser 

import traceback
import logging 
import json
import sys

from matplotlib import pyplot as plt
from argparse import ArgumentParser
from time import gmtime, strftime
from boids import BoidsMethod

## Global variables allow me to test the command line
## Once tested one would usually put them back at the top of command function
parser = ArgumentParser(prog="Boids", description = "The Boids Flocking Bird Simulation")
parser.add_argument('--config','-c',help='Please select a config file',default='config.cfg')


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
	
	args = parser.parse_args()
	
	
	try : 
		configuration = ConfigParser.ConfigParser()
		with open(args.config) as c:
			configuration.readfp(c)
			
			## Use data specific getters and setters, e.g getint for int and getfloat for float. First argument is in the [] within the config file is the section of the data
			
			## NOTE: json.loads is required when picking up arrays etc from config file
			
			#Load boids main data [Boids]
			count = configuration.getint('Boids','count')
			frames = configuration.getint('Boids','frames')
			interval = configuration.getint('Boids','interval')
			position_bounds = json.loads(configuration.get('Boids','position_bounds'))
			velocity_bounds = json.loads(configuration.get('Boids','velocity_bounds'))
			
			#Load axis data [Axis_limits]
			xlim = json.loads(configuration.get('Axis_limits','xlim'))
			ylim = json.loads(configuration.get('Axis_limits','ylim'))
			
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
		tracker = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		print "THERE HAS BEEN AN ERROR WITH LOADING THE CONFIGURATIONS INTO THIS PROGRAMME AT %s" % tracker
		logging.error(traceback.format_exc())