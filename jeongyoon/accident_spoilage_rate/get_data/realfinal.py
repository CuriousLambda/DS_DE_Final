import requests
import pprint
import time
import json
import csv

# 코드 불러오는 함수
def get_code(url, data):
    # [코드.텍스트, , , ]
    full_code_list = []
    # [코드, , , ]
    code_list = []
    # request
    res = requests.post(url, data=data)
    resj = res.json()
    # 받은 데이터에서 코드, 텍스트를 리스트에 담음
    for i in range(len(resj)):
        acdSrhCode = resj[i]["acdSrhCode"]
        acdSrhCodeNm = resj[i]["acdSrhCodeNm"]
        full_code_list.append(acdSrhCode +"."+ acdSrhCodeNm)
        code_list.append(acdSrhCode)
    # 두 리스트 리턴
    return full_code_list, code_list

# 비율 불러오는 함수
def get_rate(url, data):
    # [내 과실 , 상대 과실]
    rate_list = []
    res = requests.post(url, data=data)
    resj = res.json()
    for i in range(len(resj)):
        my_rate = resj[i]["fltRtA"]
        your_rate = resj[i]["fltRtB"]
        rate_list.append(my_rate)
        rate_list.append(your_rate)    
    return rate_list
    

# url
A_url = "https://accident.knia.or.kr/selectCodeList1"
B_url = "https://accident.knia.or.kr/selectCodeList2"
C_url = "https://accident.knia.or.kr/selectCodeList3"
D_url = "https://accident.knia.or.kr/selectCodeList4"
rate_url = "https://accident.knia.or.kr/selectAccidentRate"
# 저장할 dict
res_dict = {}

######################################################################
# 저장될 파일 이름, acdNttyDsCode 바꿔야함 (for문 만들기 귀찮아서 수동 조작)      #
# case_code = {"cvc": 1, "highway": 2, "cvm": 3, "cva": 4, "cvb": 5} #
######################################################################

# 코드, 텍스트로 저장할 csv
f = open('./data/cvb_text.csv', 'a')
writer = csv.writer(f)

# A코드 request
A_data = {"acdNttyDsCode":5}
A_full_code_list, A_code_list = get_code(A_url, A_data)
###########
A_dict={}
A_list=[]
###########

# 각 A코드에 대해서 B코드 가져오기
for i in range(len(A_full_code_list)):
    # A코드
    codeA = A_code_list[i]
    # B코드 request
    B_data = {"acdNttyDsCode":5, "acdPlaceCodeA":codeA}
    B_full_code_list, B_code_list = get_code(B_url, B_data)
    ###########
    B_dict={}
    B_list=[]
    ###########
    # A코드 csv에 저장
    writer.writerow(A_full_code_list[i].split("."))

    # 각 B코드에 대해서 C코드 가져오기
    for j in range(len(B_full_code_list)):
        # B코드
        codeB = B_code_list[j]
        # C코드 request
        C_data = {"acdNttyDsCode":5, "acdPlaceCodeA":codeA, "acdPlaceCodeB": codeB}
        C_full_code_list, C_code_list = get_code(C_url, C_data)
        ############
        C_dict={}
        C_list=[]
        ############
        # B코드 csv에 저장
        writer.writerow(B_full_code_list[j].split("."))

        # 각 C코드에 대해서 D코드 가져오기
        for k in range(len(C_full_code_list)):
            # C코드
            codeC = C_code_list[k]
            # D코드 request
            D_data = {"acdNttyDsCode":5, "acdPlaceCodeA":codeA, "acdPlaceCodeB": codeB, "acdTargetA": codeC}
            D_full_code_list, D_code_list = get_code(D_url, D_data)
            #############
            D_dict={}
            D_list=[]
            #############
            # C코드 csv에 저장
            writer.writerow(C_full_code_list[k].split("."))

            # 각 D코드에 대해서 rate 가져오기
            for l in range(len(D_full_code_list)):
                # D코드
                codeD = D_code_list[l]
                # rate request
                D_data = {"acdNttyDsCode":5, "acdPlaceCodeA":codeA, "acdPlaceCodeB": codeB, "acdTargetA": codeC, "acdTargetB": codeD}
                rate = get_rate(rate_url, D_data)
                my_rate = rate[0]
                your_rate = rate[1]
                #############
                # {D1:[rate1,rate2], , , }
                D_dict[codeD] = rate
                # rate 전부 가저왔으면 딕셔너리를 리스트로 (C코드의 value에 넣을 예정)
                if len(D_dict) == len(D_full_code_list):
                    D_list.append(D_dict)                   
                # print(D_list)
                writer.writerow(D_full_code_list[l].split("."))
                #############
            
            C_dict[codeC] = D_list
            if len(C_dict) == len(C_full_code_list):
                C_list.append(C_dict)

        B_dict[codeB] = C_list
        if len(B_dict) == len(B_full_code_list):
            B_list.append(B_dict)

    A_dict[codeA] = B_list
    if len(A_dict) == len(A_full_code_list):
        A_list.append(A_dict)

time.sleep(1)


with open("./data/cvb_code.json", 'a', encoding='euc-kr') as f:
    json.dump(A_dict,f)
f.close()