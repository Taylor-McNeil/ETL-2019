from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from .FlexFile.Database.Database import Database
from .FlexFile.RepoScanner import RepoScanner
from .FlexFile.Admin import Admin
import json

# Create your views here.
"""
class testClass(viewsets.ViewSet):
    def create(self, request, format=None):
        try:
            print(self)
            return JsonResponse("POST was not a fail",safe=False)
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
"""

#rule creation page
@api_view(["POST"])
def rule_submission(input):
    try:
        data_capture = json.loads(input.body)[0]
        admin = Admin(data_capture)
        rule_result = admin.check_for_rule()
        response_dict = {
            'Success': 'Rule has been submitted for ' + str(data_capture['file_name']),
            'Failure': 'Rule already exists for ' + str(data_capture['file_name'])
        }
        if rule_result:
            return JsonResponse(response_dict['Success'], safe=False)
        else:
            return JsonResponse(response_dict['Failure'], safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

#sync button on dashboard
@api_view(["POST"])
def sync(input):"""
    try:
        rs = RepoScanner()
        file_result = rs.run_scanner()
        response_dict = {
            'Success': 'Database has been updated',
            'Failure': 'Database has not been updated'
        }
        if file_result:
            return JsonResponse(response_dict['Success'], safe=False)
        else:
            return JsonResponse(response_dict['Failure'], safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)"""

#dashboard page
@api_view(["GET"])
def get_rules(input):
    
    """
    try:
        db = Database()
        rules = db.get_rules()
        print(rules)
        print(type(rules))
        return JsonResponse(json.dumps(rules, ensure_ascii=False), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)"""
    
    dashboardTable = [{'file_id': 1,
                        'file_name': 'f1.txt', 
                        'last_update': '2019-11-19 19:23:02'}, 
                        {'file_id': 2, 
                        'file_name': 'sample_web_file.csv', 
                        'last_update':'2019-11-19 20:16:18'}
                        ]
    return JsonResponse(dashboardTable, safe=False)

#to get data for particular file for history page
@api_view(["GET"])
def get_file_history(input):
    """
    try:
        data_capture = json.loads(input.body)[0]
        db = Database()
        file_history = db.get_file_history(data_capture)
        return JsonResponse(json.dumps(file_history, ensure_ascii=False), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)"""
    history = [
		{
		'file_name': 'f1.txt',
		'date_uploaded': '2019-11-10 13:12:53',
		'rows': 2
		},
		{
		'file_name': 'f1.txt',
		'date_uploaded': '2019-11-10 13:12:53',
		'rows': 3
		}]
    return JsonResponse(history, safe=False)


@api_view(["GET"])
def get_file_data(input):
    """
    try:
        data_capture = json.loads(input.body)[0]
        db = Database()
        file_data = db.get_file_data(data_capture)
        return JsonResponse(json.dumps(file_data, ensure_ascii=False), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)"""
    data = [
    {'name': 'rao', 'age': '40', 'profession': 'risk management'}, 
    {'name': 'john', 'age': '35', 'profession': 'technology'},
    {'name': 'kyle', 'age': '29', 'profession': 'finance'}
    ]
    return JsonResponse(data, safe=False)


@api_view(["POST"])
def testPost(input):
    try:
        info = json.loads(input.body)
        print(info)
        return JsonResponse("POST was not a fail", safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def testGet(input):
    return JsonResponse("GET was not a fail", safe=False)


# Change these names for uniformity - file_id, file_name, last_update
@api_view(["GET"])
def getDashboard(input):
    """dashboardTable = [{"fileID": 1,
                       "fileName": "file1",
                       "lastUpdate": "11/16/19"},
                      {"fileID": 2,
                       "fileName": "file2",
                       "lastUpdate": "11/16/19"},
                      {"fileID": 3,
                       "fileName": "file3",
                       "lastUpdate": "11/16/19"},
                      ]"""
    dashboardTable = [{'file_id': 1,
                        'file_name': 'f1.txt', 
                        'last_update': '2019-11-19 19:23:02'}, 
                        {'file_id': 2, 
                        'file_name': 'sample_web_file.csv', 
                        'last_update':'2019-11-19 20:16:18'}
                        ]
    return JsonResponse(dashboardTable, safe=False)
