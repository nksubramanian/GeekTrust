# Read Me
## What's done
- The intention of the code is to meet the requirement as specified in docs/Geektrust_in_traffic_Python.pdf
- The code is developed using Python 3.8 using Virtual environment for package isolation


## Pre-requisites  
- There is no package dependency for production code and unittests 
- However, there is a package dependency for coverage that is outlined in requirements.txt


## Running
### Production code
- The command to run the application is `python -m geektrust ./inputfile/input1.txt`

### Tests
- The command to run unit test is `python -m unittest`

### Coverage
- The commands to run coverage are
```
pip install -r requirements.txt
coverage run --omit=venv/*,tests/* -m unittest
coverage html
```
- The coverage report is available at `htmlcov\index.html`
