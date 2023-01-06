from django.shortcuts import render
import json
import csv
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, "index.html")

def test1(request):
    data = request.body.decode('utf-8')[-1]
    print("################\n", data, type(data), len(data), "\n##############")
    res_dict = {}
    if data == '1':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvc_code.json') as jf:
            jsondata = json.load(jf)
            keys = jsondata.keys()
            with open ('/Users/admin/Desktop/final/data/cvc_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in keys:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)
    elif data == '2':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/highway_code.json') as jf:
            jsondata = json.load(jf)
            keys = jsondata.keys()
            with open ('/Users/admin/Desktop/final/data/highway_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in keys:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)
    elif data == '3':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvm_code.json') as jf:
            jsondata = json.load(jf)
            keys = jsondata.keys()
            with open ('/Users/admin/Desktop/final/data/cvm_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in keys:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)
    elif data == '4':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cva_code.json') as jf:
            jsondata = json.load(jf)
            keys = jsondata.keys()
            with open ('/Users/admin/Desktop/final/data/cva_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in keys:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)
    else:
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvb_code.json') as jf:
            jsondata = json.load(jf)
            keys = jsondata.keys()
            with open ('/Users/admin/Desktop/final/data/cvb_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in keys:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)


def test2(request):
    data = request.body.decode('utf-8')
    print("@@@@@@@@@@@@@@@\n", data, type(data), len(data), "\n@@@@@@@@@@@@@")
    main_code = data.split('&')[0][-1]
    code_A = data.split('&')[1][7:]
    print(main_code)
    print(code_A)
    res_dict = {}

    if main_code == '1':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvc_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A]:
                code_B_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cvc_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_B_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    elif main_code == '2':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/highway_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A]:
                code_B_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/highway_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_B_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    elif main_code == '3':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvm_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A]:
                code_B_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cvm_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_B_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    elif main_code == '4':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cva_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A]:
                code_B_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cva_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_B_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    else:
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvb_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A]:
                code_B_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cvb_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_B_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)
    
def test3(request):
    data = request.body.decode('utf-8')
    print("@@@@@@@@@@@@@@@\n", data, type(data), len(data), "\n@@@@@@@@@@@@@")
    main_code = data.split('&')[0][-1]
    code_A = data.split('&')[1][7:]
    code_B = data.split('&')[2][7:]
    print(main_code)
    print(code_A)
    print(code_B)
    res_dict = {}

    if main_code == '1':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvc_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B]:
                code_C_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cvc_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_C_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    elif main_code == '2':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/highway_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B]:
                code_C_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/highway_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_C_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    elif main_code == '3':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvm_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B]:
                code_C_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cvm_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_C_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    elif main_code == '4':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cva_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B]:
                code_C_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cva_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_C_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    else:
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvb_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B]:
                code_C_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cvb_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_C_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

def test4(request):
    data = request.body.decode('utf-8')
    print("@@@@@@@@@@@@@@@\n", data, type(data), len(data), "\n@@@@@@@@@@@@@")
    main_code = data.split('&')[0][-1]
    code_A = data.split('&')[1][7:]
    code_B = data.split('&')[2][7:]
    code_C = data.split('&')[3][7:]
    print(main_code)
    print(code_A)
    print(code_B)
    print(code_C)
    res_dict = {}

    if main_code == '1':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvc_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B][0][code_C]:
                print(i)
                code_D_list = i.keys()
                print(code_D_list)
            with open ('/Users/admin/Desktop/final/data/cvc_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_D_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    elif main_code == '2':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/highway_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B][0][code_C]:
                code_D_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/highway_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_D_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    elif main_code == '3':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvm_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B][0][code_C]:
                code_D_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cvm_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_D_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    elif main_code == '4':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cva_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B][0][code_C]:
                code_D_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cva_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_D_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

    else:
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvb_code.json') as jf:
            jsondata = json.load(jf)
            for i in jsondata[code_A][0][code_B][0][code_C]:
                code_D_list = i.keys()
            with open ('/Users/admin/Desktop/final/data/cvb_text.csv', 'r') as cf:
                reader = csv.reader(cf)
                for row in reader:
                    if row[0] in code_D_list:
                        res_dict[row[0]] = row[1]
                        continue
        print(res_dict)
        return JsonResponse(res_dict)

def test5(request):
    data = request.body.decode('utf-8')
    print("@@@@@@@@@@@@@@@\n", data, type(data), len(data), "\n@@@@@@@@@@@@@")
    main_code = data.split('&')[0][-1]
    code_A = data.split('&')[1][7:]
    code_B = data.split('&')[2][7:]
    code_C = data.split('&')[3][7:]
    code_D = data.split('&')[4][7:]
    print(main_code)
    print(code_A)
    print(code_B)
    print(code_C)
    print(code_D)

    if main_code == '1':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvc_code.json') as jf:
            jsondata = json.load(jf)
            rate_list = jsondata[code_A][0][code_B][0][code_C][0][code_D]
        print(rate_list)
        return HttpResponse(rate_list[0])

    elif main_code == '2':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/highway_code.json') as jf:
            jsondata = json.load(jf)
            rate_list = jsondata[code_A][0][code_B][0][code_C][0][code_D]
        print(rate_list)
        return HttpResponse(rate_list[0])

    elif main_code == '3':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvm_code.json') as jf:
            jsondata = json.load(jf)
            rate_list = jsondata[code_A][0][code_B][0][code_C][0][code_D]
        print(rate_list)
        return HttpResponse(rate_list[0])

    elif main_code == '4':
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cva_code.json') as jf:
            jsondata = json.load(jf)
            rate_list = jsondata[code_A][0][code_B][0][code_C][0][code_D]
        print(rate_list)
        return HttpResponse(rate_list[0])

    else:
        with open('/Users/admin/Desktop/final/django_practice/final_practice/final_practice/static/cvb_code.json') as jf:
            jsondata = json.load(jf)
            rate_list = jsondata[code_A][0][code_B][0][code_C][0][code_D]
        print(rate_list)
        return HttpResponse(rate_list[0])