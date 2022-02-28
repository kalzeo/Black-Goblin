:: IMPORTANT: make sure there's no spaces between the variable and it's value i.e. set test="test", set test=0, etc.
:: Class indexes for the classes variable must seperated by spaces after the first number i.e. 0 1 2

@echo off
set proj="./tests/SCENE_BadBlood"     & :: The directory for the project, paste the path between the quotes
set name="SCENE_BadBlood_yolov5l"     & :: The project name
set src="./videos/SCENE_BadBlood.mp4" & :: Path to the video
set classes=0                         & :: The class indexes for the model to identify (see 'Class Indexes.xlsx') seperated by spaces if number of classes > 1

python track.py --project %proj% --name %name% --source %src% --classes %classes%