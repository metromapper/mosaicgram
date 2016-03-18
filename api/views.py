# coding: utf8

import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def get_image(request):
    if request.method == 'GET':
        json_data = {
            "a": [
                1,2,3,4
            ]
        }
        HttpResponse.status_code = 200
        return HttpResponse(json.dumps(json_data), content_type='application/json')
    elif request.method == 'POST':
        return HttpResponse(json.dumps({"b": [1,2,3,4,5,6]}), content_type='application/json')


def image_detail(request, artboard_id):
    if request.method == 'PUT':
        return HttpResponse(json.dumps({"b": [1,2,3,4,5,6]}), content_type='application/json')
    elif request.method == 'DELETE':
        return HttpResponse(json.dumps({"b": [1,2,3,4,5,6]}), content_type='application/json')
