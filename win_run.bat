:: IMPORTANT: make sure there's no spaces between the variable and it's value i.e. set test="test", set test=0, etc.
:: The default model used is YOLOv5l. However, this default can be changed in track.py on line 261 to YOLOv5[s,n,m,l,x]

@echo off
:: The directory for the project, paste the path between the quotes
set proj="./tests/SCENE_BadBlood"

:: The project name
set name="SCENE_BadBlood_yolov5l"

:: Path to the video
set src="./videos/SCENE_BadBlood.mp4"

:: Class indexes for the model to identify. Must be seperated by spaces after the first number i.e. 0 1 2. See 'Class Indexes.xlsx' for more indexes.
set classes = 0

python track.py --project %proj% --name %name% --source %src% --classes %classes%