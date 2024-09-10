import requests
import json

import requests as reqs

def pred():
    l = input("🐳 물고기의 길이를 입력해주세요 : ")

    resp = reqs.get(f"http://localhost:8001/fish?length={l}").text
    w=eval(resp)["prediction"]
    
    resp = reqs.get(f"http://localhost:8002/fish_std?length={l}&weight={w}&nneighbor=5").text
    pred=eval(resp)["prediction"]

    print(f"\n🐳 입력한 물고기의 길이는 {l}입니다.")
    if float(w)<0:
        print(f"🐳 물고기의 무게는 너무 작아 예측이 어렵습니다.")        
    else:
        print(f"🐳 물고기의 무게는 {w}로 예측됩니다.")
    print(f"🐳 물고기의 종류는 {pred}로 예측됩니다.\n")

#def lr_api(length):
#    headers = {
#        'accept': 'application/json',
#    }
#
#    params = {
#        'length': length,
#    }
#
#    response = requests.get('http://127.0.0.1:8001/fish_linear_ml_predictor', params=params, headers=headers)
#    data=json.loads(response.text)
#    r=data['prediction']
#    return r
#
#def knn_api(length,weight,n_neighbors=5):
#    headers = {
#        'accept': 'application/json',
#    }
#
#    params = {
#        'n_neighbors': '5',
#        'length': length,
#        'weight': weight,
#    }
#
#    response = requests.get('http://127.0.0.1:8002/fish_ml_predictor', params=params, headers=headers)
#    data=json.loads(response.text)
#    r=data['prediction']
#    
#    return r
#
#
#
#def predict():
#    length = float(input("물고기의 길이를 입력하세요: "))
#
#    ## weight 예측 선형회귀 API 호출
#    weight = lr_api(length)
#
#    ## 물고기 분류 API 호출
#    fish_class = knn_api(length, weight)
#
#    print(f"🐠length:{length}(cm) 물고기는 weight:{weight}(g)으로 예측되며 종류는 {fish_class}입니다.")
