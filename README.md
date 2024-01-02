<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Real-time Object Detection in Videos</h3>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Leverages the speed and accuracy of YOLOv5 and DeepSort for real-time object detection in videos. This project identifies and tracks specified objects while providing timestamps for when the object comes in and out of view for precise analysis. Ideal for surveillance, autonomous systems, or interactive media applications.

### Built With

* [Python 3.7.9](https://www.python.org/downloads/release/python-379/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Download & Install Git from [here](https://git-scm.com/downloads) and select your OS from the list.

2. Download & Install Python 3.7.9 from [here](https://www.python.org/downloads/release/python-379/) and select your OS from the list.

3. Download & Install Python pip [**SKIP IF INSTALLED**].
   <br>
   Pip should be installed by default but if it isn't then use the respective commands.
   ```sh
   Windows / macOS:
   >> curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   >> python3.7 get-pip.py
   
   Linux:
   >> sudo apt install python3-pip
   ```
   
4. Clone the repo
   ```sh
   >> git clone https://github.com/kalzeo/Black-Goblin.git
   ```
   
5. Install packages through the terminal
   ```sh
   >> pip install -r requirements.txt
   
      OR
      
   >> pip install --user -r requirements (use this if Errno 13 is thrown)
   ```
   
6. Enable Cython Evaluation through the terminal (Optional - provides faster evaluations)
   ```sh
   Windows:
   >> win_enable_cyphon.bat
   
   Linux / macOS:
   >> chmod +x unix_enable_cython.sh
   >> sh unix_enable_cython.sh
   ```



<!-- USAGE EXAMPLES -->
## Usage

Using the supplied .bat or .sh run files. Remember to edit the .bat or .sh file before running.
   ```sh
   Windows:
   >> win_run.bat
   
   Linux / macOS:
   >> chmod +x unix_run.sh # ONLY REQUIRED ONCE TO MAKE THE FILE EXECUTABLE
   >> sh unix_run.sh
   ```

If you wish to write the script manually using terminal it can be done like so:
```sh
# If you want to track everything do not supply the --classes flag
# Class labels can be chained like so '--classes 0 1 2 ...' for tracking specific objects. See 'Class Indexes.xlsx' for more class labels. 
>> python3.7 track.py --project "ProjectDirectory" --name "ProjectName" --source "VideoPath" --classes 0
```

Specifying a specific YOLO model using the --yolo_model flag:
```sh
>> python3.7 track.py --project "ProjectDirectory" --name "ProjectName" --source "VideoPath" --classes 0 --yolo_model "yolov5s.pt"
```

Specifying a specific DeepSort model using the --deep_sort_model flag:
```sh
>> python3.7 track.py --project "ProjectDirectory" --name "ProjectName" --source "VideoPath" --classes 0 --yolo_model "yolov5s.pt" --deep_sort_model osnet_x0_5_market1501
```

<!-- DEFAULTS -->
## Default YOLOv5 / DeepSort Models

Default values for the project are set in track.py from lines 259-287. This file can be found in the projects root directory.

The default YOLOv5 model used is YOLOv5l. Typical examples that can be used are YOLOv5[s,n,m,l,x] but more examples can be found [here](https://github.com/ultralytics/yolov5#pretrained-checkpoints). 
The default YOLO model can be changed in track.py (line 261) and will be automatically downloaded when the program runs for the first time with this new default.

The default DeepSort model used is ResNet18. More examples can be found [here](https://kaiyangzhou.github.io/deep-person-reid/MODEL_ZOO). 
The default DeepSort model can be changed in track.py (line 262) and will be automatically downloaded when the program runs for the first time with this new default if the model is available for use.


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Kyle McPherson - [Email](mailto:k.mcpherson13@rgu.ac.uk)
