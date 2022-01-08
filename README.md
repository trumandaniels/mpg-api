# MPG API
## What is this project?
A RESTful API that returns mileage (MPG) and other data on specific cars. I have imported the data into a local sqlite database called auto-mpg.db from data sourced [here](https://www.kaggle.com/uciml/autompg-dataset). I have only tested on linux, but I may add Windows compatibility at a later time.

## Set Up
First (Optional) Step: create and activate python virtual environemnt or anaconda environment first (skipping this step could cause package dependency/compatibility issues if your machine is used for many projects)

Creating python virtual environment:
```
~ $ python3 -m venv /path/to/new/virtual/VIRTUALENVNAME 
```
You can activate the environment using:
```
~ $ source /path/to/new/virtual/VIRTUALENVNAME/bin/activate
```

Then install neccesary packages to run the scripts
```
(VIRTUALENVNAME) ~ $ pip install -r /path/to/requirements.txt 
```

### How to make predictions:
Run the script that starts the server (API) locally:
```
(VIRTUALENVNAME) ~ $ python3 /path/to/run_server.py
```

In a seperate console, you use the model with:

```
~ $ curl -d '{"cylinders":6,"displacement":300,"horsepower":150,"weight":3000,"acceleration":10,"modelyear":85,"origin":"American"}' -H "Content-Type: application/json" -X POST http://localhost:5000
```
example response:
```
{
  "mpg": "23.186745"
}
```

and an example script that calls the API to query the database and returns json formatted data

```
(VIRTUALENVNAME) ~ $ python3 /path/to/example_request.py
{'mpg': '23.186745'}
```
