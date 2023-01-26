Tree /a /f

|   readme.txt
|
+---Data_pre-processing
|       data_labeling_for_classification.ipynb
|       duplicate_file_del.ipynb
|       make_dataframe_for_regressor.ipynb
|       polygon_to_masking.ipynb
|       polygon_to_masking02.ipynb
|       seperate_bumper_class.py
|       seperate_damage_class.ipynb
|       seperate_damage_class.py
|
\---model_fit
    |   classification_Unimplemented.ipynb
    |   repaircost_pred_for_XGB.ipynb
    |   service_test.ipynb
    |
    +---data
    |       label_data.csv
    |       rear_bumper_df.csv
    |
    \---models
            test_XGB03.model
            [DAMAGE][Breakage_3]Unet.pt
            [DAMAGE][Crushed_2]Unet.pt
            [DAMAGE][Scratch_0]Unet.pt
            [DAMAGE][Seperated_1]Unet.pt
            [PART]Unet.pt

Data_pre-processing : 전처리 파일을 모아놓은 파일


파일 삭제
- duplicate_file_del.ipynb : image와 json파일을 match했을 때 동시에 존재하지 않는 파일을 삭제


json파일을 읽어와서 분류하는 작업
- seperate_bumper_class : bumper만 존재하는 폴더에서 json의 'Rear bumper'와 'Front bumper'를 읽어서 class를  새로운 폴더로 복사 (class별로 분류하는 작업)
- seperate_damage_class : 파손 종류별로 폴더 생성하고 image와 그 사진을 의미하는 json파일 을 복사함 (class별로 분류하는 작업)


이미지
- data_labeling_for_classification : 분류작업을 하기 위해서 해당 사진을 설명하는 json파일에서 차량 부품의 종류를 가져오고 특문 제거 후 훈련을 위해 수치형으로 라벨링하는 작업

- polygon_to_masking : json의 polygon 형태로 되어 있는 segmentation 정보를 모델에 넣을수 있는 masking 된 정보로 바꾸는 작업
- polygon_to_masking02 : json의 polygon 형태로 되어 있는 segmentation 정보를 모델에 넣을수 있는 masking 된 정보로 바꾸는 작업, 데이터 이미지로 확인


회귀모델 훈련하기 위한 dataframe 만들기
- make_dataframe_for_regressor: 파손 부위 면적은 이미지파일을 훈련된 segmentation의 prediction값을 사용해서 채우고, 차량 id, 종류, 수리비는 견적서(xlsx)파일 에서 가져와서 dataframe을 제작하였다.


model_fit
folder 
1. data : dataframe이 저장되는 폴더
2. mdoels : 훈련된 모델들이 저장되는 폴더

- classification_Unimplemented : 이미지 데이터와 그 이미지의 라벨 데이터로 훈련하려고 해보았으나 시간상 주 목표인 segmentation과 regressor를 구현하기위해 중단

- repaircost_pred_for_XGB : 전처리를 통해 만들어진 dataframe을 통해 XGB를 사용하여 모델 예측
- service_test : 말 그대로 서비스 테스트 사진 한 장과 차량 모델을 입력받으면 훈련된 segmentation 모델을 사용해 파손 면적을 구하고 그 정보를 토대로 훈련된 XGB모델의 predict값인 수리비를 output으로 보여준다.