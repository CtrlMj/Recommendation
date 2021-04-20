from flask import Flask, request
import numpy as np
import pandas as pd
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route("/")
def welcome():
	return "Welcome to homepage!"


@app.route("/predict")
def predict():
	"""
		This will predict 3 most similar laptops to the
		input query which is a laptop's full name
		---
		parameters:
			- name: 
	"""