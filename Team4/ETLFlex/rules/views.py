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
from Database.Database import Database
from RepoScanner import RepoScanner
from Admin import Admin
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


@api_view(["POST"])
def sync():
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
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def get_rules():
    try:
        db = Database()
        rules = db.get_rules()
        return JsonResponse(json.dumps(rules, ensure_ascii=False), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def get_file_history(input):
    try:
        data_capture = json.loads(input.body)[0]
        db = Database()
        file_history = db.get_file_history(data_capture)
        return JsonResponse(json.dumps(file_history, ensure_ascii=False), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def get_file_data(input):
    try:
        data_capture = json.loads(input.body)[0]
        db = Database()
        file_data = db.get_file_data(data_capture)
        return JsonResponse(json.dumps(file_data, ensure_ascii=False), safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


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


@api_view(["GET"])
def getDashboard(input):
    dashboardTable = [{"fileID": 1,
                       "fileName": "file1",
                       "lastUpdate": "11/16/19"},
                      {"fileID": 2,
                       "fileName": "file2",
                       "lastUpdate": "11/16/19"},
                      {"fileID": 3,
                       "fileName": "file3",
                       "lastUpdate": "11/16/19"},
                      ]
    return JsonResponse(dashboardTable, safe=False)
