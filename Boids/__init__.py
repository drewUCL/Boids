import json
import ConfigParser 

import traceback
import logging
import datetime 

from matplotlib import pyplot as plt
from argparse import ArgumentParser
from Boids import Boids



'''
TODO:
	1. Create configeration file
	2. Link configs
	3. Exception handling - add firther IOError etc etc

'''

def command():
	''' 
	Description: A function to communicate with the command line. This function is linked with the setup.py file.
	'''
	
	#NOTE_1: Instantiate the parser method with data
	#NOTE_2: Bring together default values
	#NOTE_3: Write code with exceptions
	
	parser = ArgumentParser(prog="Boids", description = "The Boids Flocking Bird Simulation")
	parser.add_argument('--config','-c',help='Please select a config file',default='config.cfg')
	args = parser.parse_args()
	
	configuration = ConfigParser.ConfigParser()
	
	try : 
		with open(os.path.join(os.path.dirname(__file__),'factors',args.config)) as c
			
	except Exception as e:
		tracker = datetime.now()
		print("THERE HAS BEEN AN ERROR WITH LOADING THE CONFIGURATIONS INTO THIS PROGRAMME AT %s" % datetime.strptime(tracker, "%d/%m/%y %H:%M"))
		logging.error(traceback.format_exc())