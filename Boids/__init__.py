import json

from matplotlib import pyplot as plt
from argparse import ArgumentParser
from Boids import Boids

def command():
	''' 
	Description: A function to communicate with the command line. This function is linked with the setup.py file.
	'''
	
	#NOTE_1: Instantiate the parser method with data
	#NOTE_2: Bring together default values
	#NOTE_3: Write code with exceptions
	
	parser = ArgumentParser(prog="Boids", description = "The Boids Flocking Bird Simulation")
	parser.add_argument('','',help='',default='')
	args = parser.parse_args()
	