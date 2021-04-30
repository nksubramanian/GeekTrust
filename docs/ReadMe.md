# Read Me
## What's done
- The intention of the code is to meet the requirement as specified in docs/Geektrust_in_traffic_others.pdf
- The code is developed using Python 3.8 using Virtual environment for package isolation


## Pre-requisites  
- There are no external packages needed for working of this project 


## Running
- The application's entry point is geektrust.py
- The command is `python main.py ./inputfile/input1.txt'
  

## Tests
- The integration tests and unit test can be found in tests directory
- The application is unit tested using the default framework `unittest`
- The command to run unit test is python -m unittest
- The unit test coverage is measured by `coverage`
- Command to run test coverage is `coverage run --omit=venv/*,tests/*,venv38/* -m unittest`
- Command to get coverage report is `coverage html`
- The coverage report is available at htmlcov/index.html
- **The unit test code coverage is 100%**

