from django.shortcuts import render, redirect
# from .models import User
from django.contrib import auth
import re
from .models import User, Image
from pymongo import MongoClient
from django.http import JsonResponse
from elasticsearch import Elasticsearch
from django.core.paginator import Paginator
from config import *


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "GET" :
        return render(request, 'login.html')
    elif request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')

        res_data = {}
        if username == '' or password == '':
            res_data['error'] = "모든 칸을 다 입력해주세요."
        else :
            user = User.objects.get(username=username)
            if password == user.password:
                request.session['user'] = user.id
                return redirect('/index')
            else:
                res_data['error'] = "비밀번호가 틀렸습니다."

    return render(request, 'login.html', res_data)

def signUp(request):
    userdb = User.objects.all()
    email_validation = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    phone_number_validation = re.compile('\d{2,3}-\d{3,4}-\d{4}')
    password_validation = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
    if request.method == 'GET' :
        return render(request, 'signUp.html')
    elif request.method == 'POST' :
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        res_data = {}
        if username == '' or email == '' or firstname == '' or lastname == '' or phone_number == '' or password1 == '':
            res_data['empty_error'] = '모든 정보가 입력되지 않았습니다.'
        elif password1 != password2:
            res_data['pw_error02'] = "비밀번호가 다릅니다."
        elif userdb.filter(username = username).exists():
            res_data['username_error'] = "이미 존재하는 아이디입니다."
        elif userdb.filter(phone_number = phone_number).exists():
            res_data['phone_number_error02'] = "이미 가입된 연락처입니다."
        elif email_validation.match(email) == None:
            res_data['email_error'] = '@와 .를 포함한 이메일형식이 아닙니다.'
        elif phone_number_validation.match(phone_number) == None:
            res_data['phone_number_error'] = '-를 포함한 연락처 형식이 아닙니다.'
        elif password_validation.match(password1) == None:
            res_data['pw_error01'] = '비밀번호 형식을 확인해주세요.'
        else:
            # user = User_data(
            #     username=username,
            #     password=password1,
            #     email=email,
            #     phone_number=phone_number,
            #     firstname=firstname,
            #     lastname=lastname,
            # )
            # user.save()

            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
                first_name=request.POST['firstname'],
                last_name=request.POST['lastname'],
                phone_number=request.POST['phone_number']
            )
            auth.login(request, user)
            res_data['success'] = 'ok'


        return render(request, 'signUp.html', res_data)

def main(request):
    return render(request, 'main.html')

def side01(request):
    return render(request, 'side01.html')

def side02(request):
    return render(request, 'side02.html')

def show_repairs(request):
    # 좌표값 get
    input_lat = float(request.GET.get('input_lat'))
    input_lon = float(request.GET.get('input_lon'))

    # 몽고db 연결
    client = MONGODB_CONFIG['url']
    db = client['test']

    # 좌표값에서 반경 5km 이내에 있는 데이터 검색 쿼리
    query = {'location': {'$geoWithin': {'$centerSphere': [[input_lon, input_lat], 5 / 6378.1]}}}

    # 휴점, 폐점 데이터를 제외하고 json 형식으로 변환해서 리스트에 삽입
    repair_list = list()
    for doc in db.repair.find(query):
        repair_dict = dict()
        repair_dict['자동차정비업체명'] = doc['s_name']
        repair_dict['자동차정비업체종류'] = doc['s_type']
        repair_dict['주소'] = doc['address']
        repair_dict['좌표'] = doc['location']['coordinates']
        repair_dict['영업상태'] = doc['running']
        repair_dict['운영시작시각'] = doc['open_time']
        repair_dict['운영종료시각'] = doc['close_time']
        repair_dict['전화번호'] = doc['phone_number']
        if repair_dict['영업상태'] == 1:
            repair_list.append(repair_dict)

    return JsonResponse({'list': repair_list})


def side03(request):
    return render(request, 'side03.html')

def elasticsearch(request):
    # 검색어, 영업상태, 정비소구분 get
    words = request.GET.get('words')
    s_type = request.GET.get('s_type')
    running = request.GET.get('running')

    # elasticsearch 연결
    end_point = ELASTIC_CONFIG['url']
    es = Elasticsearch(hosts=end_point)

    # 검색할 index
    index_name = 'repairs'

    # 검색 쿼리
    res = es.search(index=index_name,
                    query={
                        "query_string": {
                            "query": "(s_type: *" + s_type + ") AND (running: *" + running + ") AND (s_name: *" + words + "* OR address:*" + words + "*)"}}, size=50000)
    result_list = [el['_source'] for el in res['hits']['hits']]

    for i in range(len(result_list)):
        result_list[i]['id'] = i + 1
        result_list[i]["time"] = result_list[i]["open_time"] + " - " + result_list[i]["close_time"]

    return JsonResponse({"list": result_list})

def admin(request):
    return render(request, 'admin.html', {'list':User.objects.all()})

def main01(request):
    return render(request, 'main01.html')

def upload(request):
    res_data = {'status' : ''}
    if request.method == 'POST' :
        file = request.FILES.get('chooseFile')
        if file:
            image = Image(file=file)
            image.save()
            res_data['status'] = 'ok'
        return render(request, 'main01.html', res_data)
    return render(request, 'main01.html', res_data)

def visitor(request):
    return render(request, 'visitor.html')

def usage(request):
    return render(request, 'usage.html')

def user(request):
    return render(request, 'user.html', {'list' : User.objects.all()})