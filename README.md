# MPG API
## What is this project?
A RESTful API that estimates mileage (MPG) based on other data about a car. I have imported the data into a local sqlite database called auto-mpg.db from data sourced [here](https://www.kaggle.com/uciml/autompg-dataset). I have only tested on linux with python 3.9.4 but Windows should be compatible with some command line tweaks.

The basic idea here is that I built a keras model (with model.ipynb) with a fuel efficency dataset (auto-mpg.csv) and then serve it via API (simple_server.py).

### A couple of model notes:
The dataset itself is composed of car data with the following variables

- mpg: continuous
- cylinders: multi-valued discrete
- displacement: continuous
- horsepower: continuous
- weight: continuous
- acceleration: continuous
- model year: multi-valued discrete
- origin: multi-valued discrete
- car name: string (unique for each instance). 

I have replaced the ambigious "origin" that uses 1,2,3 as labels, to "American", "European", or "Asian". Also the dataset is only for cars from 1970 to 1993, which means cars from other years are extrapolated poorly (so keep that in mind when estimating a car from 2022).

## Set Up
First (Optional) Step: create and activate python virtual environemnt or anaconda environment first (skipping this step could cause package dependency/compatibility issues if your machine is used for many projects)

Changing the working directory to wherever you extract the downloaded folder to
```
(base) truman@laptop ~ $ cd /path/to/extracted/mpg-api-main
```

#### Creating python virtual environment:
either (after installing virtualenv) choosing a specific python version
```
(base) truman@laptop ~/mpg-api-main ~ $  virtualenv --python=/usr/bin/python3.9 /path/to/new/environment/VIRTUALENVNAME 
```
or using whatever your PATH is set to (probably fine)
```
(base) truman@laptop ~/mpg-api-main ~ $ python3 -m venv /path/to/new/environment/VIRTUALENVNAME 
```
#### You can then activate the environment using:
```
(base) truman@laptop ~/mpg-api-main ~ $ source /path/to/new/environment/VIRTUALENVNAME/bin/activate
```

Then install neccesary packages to run the scripts
```
(VIRTUALENVNAME) (base) truman@laptop ~/mpg-api-main ~ $ pip install -r requirements.txt 
```

## How to make predictions:
Run the script that starts the server (API) locally:
```
(VIRTUALENVNAME) (base) truman@laptop ~/mpg-api-main ~ $ python3 simple_server.py
```

In a seperate console, you can use the model with either:
```
(base) truman@laptop ~ $ curl -d '{"cylinders":6,"displacement":300,"horsepower":150,"weight":3000,"acceleration":10,"modelyear":85,"origin":"American"}' -H "Content-Type: application/json" -X POST http://localhost:5000
```
example response:
```
{
  "mpg": "24.301125"
}
```

or by tweaking an example script that calls the API to query the database and returns json formatted data

```
(VIRTUALENVNAME) (base) truman@laptop ~/mpg-api-main ~ $ python3 example_request.py
{'mpg': '24.301125'}
```

#### Sources:

https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html

https://curiousily.com/posts/deploy-keras-deep-learning-project-to-production-with-flask/

https://www.tensorflow.org/guide/keras/save_and_serialize

https://keras.io/examples/structured_data/structured_data_classification_from_scratch/
