Boids <br>
=============================================

This library allows a user to simulate flocking birds with the ability to change the parameters of the programme to analyse different behaviour. The models used were proposed by Craig W. Reynolds in his paper entitled *"Flocks, Herds, and Schools:
A Distributed Behavioral Model"*. A copy of this paper can be found <a href="http://www.cs.toronto.edu/~dt/siggraph97-course/cwr87" target="_blank">here</a>.

##Install Instructions

- Download Boids to your machine from GitHub
- If the download has been compressed into a zip file, extract
- Navigate to Boids folder root from your command line
- Now on your command line type:
- **Windows**    : `python Greengraph/setup.py install`
- **Other/Mac**  : `sudo python Greengraph/setup.py install`

The Boids library is now installed on your machine and ready to use. 

##Example Usage


##Parameter Config

The config file that is used as default is shown exhibited below with name placeholders. The parameters are defaulted to the values in {} if you do not choose to upload your own config file.

```
[Boids]
count = input_number_of_birds_in_flock  {50}
frames = input_number_of_frames_in_animation  {50}
interval = input_time_interval_between_frames  {50}
position_bounds = [x_min_bound, y_min_bound, x_max_bound, y_max_bound]  {[-450, 300, 50, 600] --- position limits}
velocity_bounds = [x_min_bound, y_min_bound, x_max_bound, y_max_bound]  {[0, -20, 10, 20] --- velocity limits}

[Axis_limits]
xlim = [x_axis_min,x_axis_max]  {[-500,1500]}
ylim = [y_axis_min,y_axis_max]  {[-500,1500]}

[Flock_Dynamics]
threshold = max_distance_before_forcing_into_formation  {10000}
must_fly_away = max_distance_from_another_bird_before_requiring_to_fly_towards_middle  {100}
speed_with_nearby_boids_calibration = likelyhood_of_birds_getting_too_close  {0.125} 
fly_to_middle_gravity = gravitational_pull_to_flock_center  {0.01}
```

If you try to upload your own config file and this fails, the programme will give you the option of running Boids with the default parameters.



