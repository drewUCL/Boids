import numpy as np
import yaml
import sys
import os

from nose.tools import assert_equal,assert_almost_equal,assert_not_equal
from ..__init__ import parser, command, user_run_defaults
from argparse import ArgumentParser
from mock import Mock, patch

sys.path.insert(0,'..')
from boids import BoidsMethod

class test_session(object):
	''' 
	Description: A class to test the boids methods and command init
	'''
	
	def analyse( self, arg1, arg2, type):
		if( type == 'almost_equal' ):
			#.all() as the truth value of an array > 1 element is ambiguous 
			assert_almost_equal( arg1.all(), arg2.all() )
		elif( type == 'exactly_equal' ):
			assert_equal( arg1, arg2 )
			
	def generator( self, test_data, file ):
		for point in test_data:
			before = point.pop( 'before' )
			after  = point.pop( 'after' )
			boids = BoidsMethod()
			boids.positions = np.array( before[0:2] )
			boids.velocities = np.array( before[2:4] )
			if( file == 'update_boids_1.yaml' ):
				boids.update_boids()
				self.analyse( boids.positions , np.array(after[0:2]), 'almost_equal' )
				self.analyse( boids.velocities, np.array(after[2:4]), 'almost_equal' )
			elif( file == 'fly_towards_middle_1.yaml' ):
				boids.fly_towards_middle()
				self.analyse( boids.positions , np.array(after[0:2]), 'almost_equal' )
				self.analyse( boids.velocities, np.array(after[2:4]), 'almost_equal' )
			elif( file == 'fly_away_from_nearby_boids_1.yaml' ):
				boids.fly_away_from_nearby_boids()
				self.analyse( boids.positions , np.array(after[0:2]), 'almost_equal' )
				self.analyse( boids.velocities, np.array(after[2:4]), 'almost_equal' )
			elif( file == 'try_to_match_speed_with_nearby_boids_1.yaml' ):
				boids.try_to_match_speed_with_nearby_boids()
				self.analyse( boids.positions , np.array(after[0:2]), 'almost_equal' )
				self.analyse( boids.velocities, np.array(after[2:4]), 'almost_equal' )
			elif( file == 'move_according_to_velocities_1' ):
				boids.move_according_to_velocities()
				self.analyse( boids.positions , np.array(after[0:2]), 'almost_equal' )
				self.analyse( boids.velocities, np.array(after[2:4]), 'almost_equal' )
	
	# Testing update_boids
	def test_update_boids( self ):
		with open( os.path.join(os.path.dirname(__file__), 'fixtures', 
				  'update_boids_1.yaml') ) as data:
			self.generator( yaml.load(data), 'update_boids_1.yaml' )
			
	# Testing fly_towards_middle
	def test_fly_towards_middle( self ):
		with open( os.path.join(os.path.dirname(__file__), 'fixtures',
				  'fly_towards_middle_1.yaml') ) as data:
			self.generator( yaml.load(data), 'fly_towards_middle_1.yaml' )

	# Testing fly_away_from_nearby_boids
	def test_fly_away_from_nearby_boids( self ):
		with open( os.path.join(os.path.dirname(__file__), 'fixtures', 
				  'fly_away_from_nearby_boids_1.yaml') ) as data:
			self.generator( yaml.load(data), 'fly_away_from_nearby_boids_1.yaml' )
			
	# Testing try_to_match_speed_with_nearby_boids
	def test_try_to_match_speed_with_nearby_boids( self ):
		with open( os.path.join(os.path.dirname(__file__), 'fixtures', 
				  'try_to_match_speed_with_nearby_boids_1.yaml') ) as data:
			self.generator( yaml.load(data), 'try_to_match_speed_with_nearby_boids_1.yaml' )
	
	# Testing test_move_according_to_velocities
	def test_move_according_to_velocities( self ):
		with open( os.path.join(os.path.dirname(__file__), 'fixtures',
				  'move_according_to_velocities_1.yaml')) as data:
			self.generator( yaml.load(data), 'move_according_to_velocities_1.yaml' )
			
	# Testing generate_boids_flock
	def test_generate_boids_flock( self ):
		boids = BoidsMethod()
		flock = boids.generate_boids_flock( np.array([-450.0, 300.0]), np.array([50.0, 600.0]) )
		# Ensure the generated flock is in the correct dimensions 
		# to be processed later on in the programme
		desired_dimensions = ( 2L, 50L )
		self.analyse( flock.shape, desired_dimensions, 'exactly_equal' )
	
	# Testing initiation of config file
	def test_command( self ):
		commands = parser.parse_args(['--config', 'my_config_file.cfg']) # Use default config
		self.analyse( commands.config , 'my_config_file.cfg', 'exactly_equal' )
		
	
if __name__ == "__main__":
	test_session()