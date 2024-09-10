import os

def get_model_path():
    path=os.path.dirname(os.path.abspath(__file__))
    return f"{path}/model.pkl"

