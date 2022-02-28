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
  <a href="https://github.com/kalzeo/Black-Goblin">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Black Goblin</h3>
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

Project description.

### Built With

* [Python 3.7.9](https://www.python.org/downloads/release/python-379/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   >> git clone https://github.com/kalzeo/Black-Goblin.git
   ```
2. Install packages through the terminal
   ```sh
   >> pip install -r requirements.txt
   ```
   
3. Enable Cython Evaluation through the terminal
   ```sh
   >> enable_cyphon.bat
   ```



<!-- USAGE EXAMPLES -->
## Usage

Running the tracker to detect objects in videos
   ```sh
   # remember to customize the file before running
   >> run.bat
   
   or
   
   # don't include --classes if you want to track everything
   >> python track.py --project "ProjectName" --name "" --source "VideoPath" --classes 0
   ```


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Kyle McPherson - [Email](mailto:k.mcpherson13@rgu.ac.uk)

Project Link: [https://github.com/kalzeo/Black-Goblin](https://github.com/kalzeo/Black-Goblin)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Mike](https://github.com/mikel-brostrom) for providing [Deep Sort](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch)
