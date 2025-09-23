<picture>
  <source
    srcset=".github/osu_horizontal_white.png"
    media="(prefers-color-scheme: dark)"
  />
  <source
    srcset=".github/osu_horizontal_black.png"
    media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"
  />
  <img src=".github/osu_horizontal_black.png" alt="Oregon State University Logo." height="80px" />
</picture>

# CS361: Course Project — Reading Tracker
Because you've already forgotten what you've read!

> **Note**: this repository is archived and no longer maintained.

![Last Updated](https://img.shields.io/badge/March_2023-critical?label=Last%20Updated&style=flat-square)
![Not Maintained](https://img.shields.io/badge/Not_Maintained-critical?label=Status&style=flat-square)

## About
This full-term project uses a microservices architecture to track reading completed by the user.  The project is developed using agile methodologies.  The user interface adheres to the 8 Cognitive Style Hueristics (CSH).  Data persistence is provided using Python's built-in SQLite3 library.  Microservices for this project are provided by @[jay2002shah](https://github.com/jay2002shah/).

## Getting Started
These instructions will get you a copy of the project up and running on your local machine and the others.

### Prerequisites
You need to have a machine with [Python 3.10.x](https://www.python.org/downloads/release/python-3100/) installed.
```sh
$ python --version
Python 3.10
```

## Installation
All installation is handled using `pip` or `pipenv`. The following steps will install the project dependencies.

### Build and run the program
```sh
# Terminal 1
$ git clone https://github.com/4N0NYM0U5MY7H/CS361_Course_Project
$ cd CS361_Course_Project
$ pipenv install
$ cd microservice
$ pipenv run microservice.py
```
```sh
# Terminal 2
$ cd CS361_Course_Poject/app
$ python main.py
```
## TODO
Refer to the [Project Roadmap](https://github.com/users/4N0NYM0U5MY7H/projects/1/views/4), [Milestones](https://github.com/4N0NYM0U5MY7H/CS361_Course_Project/milestones), and [Issues](https://github.com/4N0NYM0U5MY7H/CS361_Course_Project/issues) for the current task list.

## Built With
[![Python v3.10](https://img.shields.io/badge/v3.10-3776AB?label=Python&labelColor=141414&logo=python&style=flat-square)](https://www.python.org/)
[![CS361 Microservice by Jay Shah](https://img.shields.io/badge/@jay2002shah-D73F09?label=CS%20361%20Microservice&labelColor=141414&style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAQCAYAAADNo/U5AAACCUlEQVQoU21SS4ipURz/fRJqJt2JTEnNLO7spChLZTVKKakpxcpjVrMf5MZCjc0oK5NYTLOxU+rWKEsLJZtZuCFsKVKDvJ17zrmXO7invs7j+z9+j7+AozWbzXrRaPSS7kgmk21BEL4fxwhfH97f34nFYoFOp8PHxweur69Rr9eh1+vRbDb3sfvD4+Mjicfjx0Xh9XqRzWZBOx4m3d7ekmKxCIVCgeFwyBONRiOq1Sr6/T6WyyXC4TBMJhP8fr8gEEJ+0hgrC3x6ekIoFML9/T3S6fRJV4PBgFqt9kOQSqVEpVKBkofH42EwUCgUsF6v4XA4eCI7i8Vifr66uoJAq5NgMIjtdovVagWJRMITKQK+s/X8/IxIJILJZAK73Q7h9fWV+Hw+DAYDyOVyNBoNWK1WtNtttFot3Nzc7GEyTkxZgbYl4/EYMpkMuVwOTqeTdxWJRCec2AODKfR6vZFarf729vYGl8uFRCLBlZpOp7i4uMDDwwNisRjy+TznOJ/Pf3HQFD/Z4We+vLy88Iqfn58IBAJIpVK861+ef5hSb4hSqeSP7DObzahUKnC73chkMlwQpnCn08H5+fk/l6lqhJnY7XbBhCmVSri7u+NWaLXanfG8ycHsUfIc5maz2UtOfeTQFovF6eztpKJzxodWo9FgNBqhXC7DZrMdFD+4fNX47OyMUAX/+/83AuTd2zt8GaUAAAAASUVORK5CYII=)](https://github.com/jay2002shah/)

## License
This project is licensed under the MIT License - see the [LICENSE](license) file for details.
