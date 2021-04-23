from flask import jsonify, request
import numpy as np
import pandas as pd
app = Flask(__name__)


#load the original dataset
df = pd.read_csv("Final_Dataframe.csv")
#load trained similarity matrix
similarity_mtrx = np.load("similarity_mtrx.npy")




@app.route("/predict")
def predict():
    
    laptop_name = request.args.get("laptopName")
    id = df[ df['laptop_name'] == laptop_name ].index[0]
    try:
        similar_ids = similarity_mtrx[id, 1:4]
        #similars = [df.loc[i, 'brand'] + ' ' + df.loc[i, 'laptop_name'] for i in similar_ids]
        return jsonify(df.iloc[similar_ids]), 200
    except Exception as e:
        return jsonify(str(e)), 500