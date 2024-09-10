from typing import Union
import pickle
from fastapi import FastAPI
from fr.manager import get_model_path

app = FastAPI()

### 모델 불러오기
pkls=get_model_path()


with open(pkls, "rb") as f:
    linearfish_model = pickle.load(f)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/fish_linear_ml_predictor")
def fish(length:float):
    """
    물고기의 무게 판별기

    Args:
        length (float) : 물고기 길이(cm)

    Returns:
        dict: 입력받은 물고기의 길이와 예측된 무게를 반환

    """
    # 물고기 무게 예측 
    prediction = float(linearfish_model.predict([[length]])[0][0])

    # 물고기 길이와 무게 반환 - 나올 수 있음 
    return {     
                "length" : length,
                "prediction" : prediction 
           }
