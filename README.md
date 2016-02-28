Boids <br>
=============================================

This library allows a user to simulate flocking birds with the ability to change the parameters of the programme to analyse different behaviour. The models used were proposed by Craig W. Reynolds in his paper entitled *"Flocks, Herds, and Schools:
A Distributed Behavioral Model"*. A copy of this paper can be found <a href="http://dl.acm.org/citation.cfm?doid=37401.37406" target="_blank">here</a>.

##Install Instructions

- Download Boids to your machine from GitHub
- If the download has been compressed into a zip file, extract
- Navigate to Boids folder root from your command line
- Now on your command line type:
- **Windows**    : `python Boids/setup.py install`
- **Other/Mac**  : `sudo python Boids/setup.py install`

The Boids library is now installed on your machine and ready to use. 

##Example Usage

After install of the programme, you can run it using the follwoing command:

+ `Boids --config config_file_location.cfg`

The above command has the optional parameter of --config (or -c if you would like to use the shortcut). You do not need to specify a configuration file as it will default to the parameters shown in **Parameter Config**. To simply run the programme with the default configuration just run `Boids` in your command line.

If you wish to specify your own config file please refer to the section below for further assistance.

##Parameter Config

The config file that is used as default is shown exhibited below with name placeholders. If you are going to load your own config file then please format as below:

**Note:** You do not need to fill in all the parameters (it will just use the default parameters). However you **must** specify each section in the config file: `[Boids], [Axis_limits], [Flock_Dynamics]`
```
[Boids]
count = input_number_of_birds_in_flock
frames = input_number_of_frames_in_animation
interval = input_time_interval_between_frames
position_bounds = [x_min_bound, y_min_bound, x_max_bound, y_max_bound]
velocity_bounds = [x_min_bound, y_min_bound, x_max_bound, y_max_bound]

[Axis_limits]
xlim = [x_axis_min,x_axis_max]
ylim = [y_axis_min,y_axis_max]

[Flock_Dynamics]
threshold = max_distance_before_forcing_into_formation
must_fly_away = max_distance_from_another_bird_before_requiring_to_fly_towards_middle
speed_with_nearby_boids_calibration = likelyhood_of_birds_getting_too_close  
fly_to_middle_gravity = gravitational_pull_to_flock_center
```

The parameters are defaulted to the values in the table if you do not choose to upload your own config file.

| Parameters                          | Default Value                        | Description   |
| ----------------------------------- |:------------------------------------:| :------------:|
| count                               | 50                                   | Number of birds in the flock |
| frames                              | 50                                   | Number of frames in the animation |
| Interval                            | 50                                   | The amount of time that passes between each animation |
| position_bounds                     | [-450, 300, 50, 600]                 | The start position limits of the flock |
| velocity_bounds                     | [0, -20, 10, 20]                     | The start velocity limits of the flock |
| xlim                                | [-500,1500]                          | The x axis bound range |
| ylim                                | [-500,1500]                          | The y axis bound range |
| threshold                           | 1000                                 | The maximum distance a bird can be seperated by before forcing it back into the formation |
| must_fly_away                       | 100                                  | The maximum distance to another bird before forcing a bird to fly towards the flock center |
| speed_with_nearby_boids_calibration | 0.125                                | The possibility of a bird betting too close to another |
| fly_to_middle_gravity               | 0.01                                 | The gravitational pull force implied to force a bird to fly towards the center of the flock |

If you try to upload your own config file and this fails, the programme will give you the option of running Boids with the default parameters.



