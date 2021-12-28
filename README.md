# mpg-api
An RESTful API that returns mileage (MPG) and other data on specific cars. I have imported the data into a local sqlite database called auto-mpg.db from data sourced [here](https://archive.ics.uci.edu/ml/datasets/auto+mpg). I have only tested on linux, but I may add Windows compatibility at a later time.

## Set Up
First (Optional) Step: create and activate python virtual environemnt or anaconda environment first (skipping this step could cause package dependency/compatibility issues if your machine is used for many projects)

Creating python3 virtual environment:
```
python3 -m venv /path/to/new/virtual/VIRTUALENVNAME 
```
You can activate the environment using:
```
source /path/to/new/virtual/VIRTUALENVNAME/bin/activate
```
note: I am not testing with anaconda but it should still work

Then install neccesary packages to run the scripts
```
(VIRTUALENVNAME) $ pip install -r /path/to/requirements.txt 
```

### In seperate console tabs (each running the python environment) 
Run the script that starts the server (API) locally:
```
(VIRTUALENVNAME) $ python3 run_server.py
```

and an example script that calls the API to query the database and returns json formatted data

```
(VIRTUALENVNAME) $ python3 example_requests.py
```
