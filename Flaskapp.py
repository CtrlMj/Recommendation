from flask import Flask, request
import numpy as np
import pandas as pd
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


#load the original dataset
df = pd.read_csv("Final_Dataframe.csv")
#load trained similarity matrix
similarity_mtrx = np.load("similarity_mtrx.npy")


@app.route("/")
def welcome():
    return "Welcome to homepage!"


@app.route("/predict")
def predict():
    """This will predict 3 most similar laptops to the
    input query which is a laptop's full name
    ---
    parameters:
        - name: laptopName
          in: query
          type: string
          required: true
    responses:
        200:
            description: The output Values
    """
    laptop_name = request.args.get("laptopName")
    id = df[ df['laptop_name'] == laptop_name ].index[0]
    similar_ids = similarity_mtrx[id, 1:4]
    similars = [df.loc[i, 'brand'] + ' ' + df.loc[i, 'laptop_name'] for i in similar_ids]
    return ' - '.join(similars)


if __name__ == "__main__":
    app.run(host='localhost', port=6006)