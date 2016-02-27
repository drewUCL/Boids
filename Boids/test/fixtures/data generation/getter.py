import yaml
import james
from copy import deepcopy

# fixture
# fly_away_from_nearby_boids_1
# fly_towards_middle_1
# try_to_match_speed_with_nearby_boids_1
# move_according_to_velocities_1
# update_boids

before=deepcopy(james.boids)
james.update_boids(james.boids)
after=james.boids
fixture={"before":before,"after":after}
fixture_file=open("update_boids_1.yaml",'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()