# Testing regression
import os
import yaml
import numpy as np

from ..boids import BoidsMethod
from nose.tools import assert_equal, assert_almost_equal

def test_bad_boids_regression():
	regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures' ,'regression.yml')))
	boid_data = np.array(regression_data["before"])
	boids = BoidsMethod()
	boids.positions = boid_data[0:2]
	boids.velocities = boid_data[2:4]
	boids.update_boids()
	assert_almost_equal(np.array(regression_data["after"]).all(),boid_data.all())