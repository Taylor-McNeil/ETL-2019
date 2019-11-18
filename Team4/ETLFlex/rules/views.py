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
def testPost(input):
    try:
        info=json.loads(input.body)
        print(info)
        return JsonResponse("POST was not a fail",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def testGet(input):
    return JsonResponse("GET was not a fail",safe=False)

@api_view(["GET"])
def getDashboard(input):
    dashboardTable =  [ {"fileID" : 1,
                        "fileName" : "file1", 
                        "lastUpdate" : "11/16/19"},
                        {"fileID" : 2,
                        "fileName" : "file2", 
                        "lastUpdate" : "11/16/19"}, 
                        {"fileID" : 3, 
                        "fileName" : "file3", 
                        "lastUpdate" : "11/16/19"},
    ]
    return JsonResponse(dashboardTable, safe = False)