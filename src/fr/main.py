from typing import Union
import pickle
from fastapi import FastAPI
from fr.model.manager import get_model_path

with open(get_model_path(), "rb") as f:
    fish_model=pickle.load(f)

app = FastAPI()

@app.get("/fish")
def fish(length:float):
    """
    물고기 무게 예측기

    Args:
     - length(int): 물고기 길이(cm)

    Return
     - dict, 물고기의 길이를 담은 딕셔너리
    """

#    with open(f"{os.path.dirname(get_model_path())}/std-model-{nneighbor}.pkl", "rb") as f:
#        fish_model=pickle.load(f)

    pred=fish_model.predict([[length**2,length]])


    return {
            "prediction":pred[0],
            "length":length,
            }
