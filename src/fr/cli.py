
def predict():
    length = float(input("물고기의 길이를 입력하세요: "))

    ## weight 예측 선형회귀 API 호출
    weight = lr_api(length)

    ## 물고기 분류 API 호출
    fish_class = knn_api(length, weight)

    print(f"🐠length:{length}(cm) 물고기는 weight:{weight}(g)으로 예측되며 종류는 {fish_class}입니다.")
