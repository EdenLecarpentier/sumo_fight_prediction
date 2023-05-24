from typing import Union
from flask_restful import Resource
import pandas as pd 
import pickle
from fastapi import FastAPI

app = FastAPI()
model = pickle.load(open('model_pkl.pickle', 'rb'))
df = pd.read_csv('18_features_df.csv')
df = df.drop(['Unnamed: 0'], axis=1)
@app.get("/")
def read_root():
    
    
    dataset['prediction'] = model.predict(dataset[[1 , 0]])
    return(prediction)
read_root()
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}