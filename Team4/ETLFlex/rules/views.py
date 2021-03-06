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


@api_view(["POST"])
def rule_submission(input):
    # Input json must have rule data with the exception of optional entries (see test_rule.py)
    try:
        data_capture = json.loads(input.body)
        admin = Admin(data_capture)
        rule_result = admin.check_for_rule()
        response_dict = {
            'Success': 'Rule has been submitted for ' + str(data_capture['file_name']),
            'Failure': 'Rule already exists for ' + str(data_capture['file_name'])
        }
        if not rule_result:
            return JsonResponse(response_dict['Success'], safe=False)
        else:
            return JsonResponse(response_dict['Failure'], safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def sync(input):
    # Input json must have file_name
    try:
        data_capture = json.loads(input.body)
        rs = RepoScanner()
        file_result = rs.file_sync(data_capture['file_name'])
        response_dict = {
            'Success': 'File has been updated',
            'Failure': 'File has not been updated'
        }
        if file_result:
            return JsonResponse(response_dict['Success'], safe=False)
        else:
            return JsonResponse(response_dict['Failure'], safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_rules(input):
    # No input required
    try:
        db = Database()
        rules = db.get_rules()
        return JsonResponse(rules, safe=False, content_type=json)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def get_file_history(input):
    # Input json must have file_name
    try:
        data_capture = json.loads(input.body)
        db = Database()
        file_history = db.get_file_history(data_capture)
        return JsonResponse(file_history, safe=False, content_type=json)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def get_file_data(input):
    # Input json must have file_name and date_uploaded from record clicked by user
    try:
        data_capture = json.loads(input.body)
        db = Database()
        file_data = db.get_file_data(data_capture)
        return JsonResponse(file_data, safe=False, content_type=json)
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


# Change these names for uniformity - file_id, file_name, last_update
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
