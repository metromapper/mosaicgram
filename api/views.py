# coding: utf8

import json

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from api.models import (
    Artboard,
    ArtboardOwnerRelation,
    IngredientImages,
)


def get_image(request):
    if request.method == 'GET':
        artboard = []
        artboard_obj = Artboard.objects.all()
        for artboard in artboard_obj:
            tmp = {}
            tmp['artboardId'] = artboard.id
            tmp['artboardTitle'] = artboard.title
            tmp['hashtag'] = artboard.hash_tag
            tmp['imageURL'] = artboard.image_url
            tmp['owners'] = []
            owner_obj = ArtboardOwnerRelation.objects.filter(artboard_id=artboard.id).all()
            for owner in owner_obj:
                tmp_owner = {}
                tmp_owner['accountId'] = owner.account_id
                tmp_owner['displayName'] = owner.display_name
                tmp['owners'].append(tmp_owner)
            artboard.append(tmp)
        HttpResponse.status_code = 200
        return HttpResponse(json.dumps(artboard), content_type='application/json')
    elif request.method == 'POST':
        json_data = json.loads(request.POST['data'])
        artboard_obj = Artboard(
            title = json_data['artboardTitle'],
            hash_tag = json_data['hashtag'],
            image_url = json_data['imageURL'],
        )
        artboard_obj.save()
        registered_artboard = Artboard.objects.get(
            title=json_data['artboardTitle'],
            hash_tag=json_data['hashtag'],
            image_url=json_data['imageURL']
        )
        result = {}
        result['artboardId'] = registered_artboard.id
        result['artboardTitle'] = registered_artboard.title
        result['hashtag'] = registered_artboard.hash_tag
        result['imageURL'] = registered_artboard.image_url
        result['owners'] = []
        owner_obj = ArtboardOwnerRelation.objects.filter(artboard_id=registered_artboard.id).all()
        for owner in owner_obj:
            tmp_owner = {}
            tmp_owner['accountId'] = owner.account_id
            tmp_owner['displayName'] = owner.display_name
            result['owners'].append(tmp_owner)
        HttpResponse.status_code = 201
        return HttpResponse(json.dumps(result), content_type='application/json')


def image_detail(request, artboard_id):
    if request.method == 'GET':
        artboard = Artboard.objects.get(id=artboard_id)
        result = {}
        result['artboardId'] = artboard.id
        result['artboardTitle'] = artboard.title
        result['hashtag'] = artboard.hash_tag
        result['imageURL'] = artboard.image_url
        result['sizeX'] = artboard.site_x
        result['sizeY'] = artboard.site_y
        result['owners'] = []
        result['images'] = []
        owner_obj = ArtboardOwnerRelation.objects.filter(artboard_id=artboard.id).all()
        for owner in owner_obj:
            tmp_owner = {}
            tmp_owner['accountId'] = owner.account_id
            tmp_owner['displayName'] = owner.display_name
            result['owners'].append(tmp_owner)
        image_objs = IngredientImages.objects.filter(artboard_id=artboard.id).all()
        for image_obj in image_objs:
            tmp_owner = {}
            tmp_owner['imageURL'] = image_obj.image_url
            tmp_owner['positionX'] = image_obj.position_x
            tmp_owner['positionY'] = image_obj.position_y
            result['images'].append(tmp_owner)
        HttpResponse.status_code = 200
        return HttpResponse(json.dumps(result), content_type='application/json')
    elif request.method == 'PUT':
        json_data = json.loads(request.POST['data'])
        artboard_obj = Artboard.objects.filter(id=artboard_id)
        artboard_data = artboard_obj.get()
        if artboard_data.title != json_data['artboardTitle']:
            artboard_obj.update(
                title=json_data['artboardTitle']
            )
        for add_data in json_data['owner_add']:
            owner_obj = ArtboardOwnerRelation(
                artboard_id=artboard_id,
                account_id=add_data['accountId'],
                display_name = add_data['displayName'],
            )
            owner_obj.save()
        for remove_data in json_data['owner_remove']:
            owner_obj = ArtboardOwnerRelation.objects.filter(
                artboard_id=artboard_id,
                account_id=remove_data['accountId'],
                display_name = remove_data['displayName'],
            )
            owner_obj.delete()
        HttpResponse.status_code = 200
        return HttpResponse(json.dumps({"status": "ok"}), content_type='application/json')
    elif request.method == 'DELETE':
        artboard = Artboard.objects.filter(id=artboard_id).delete()
        HttpResponse.status_code = 200
        return HttpResponse(json.dumps({"status": "ok"}), content_type='application/json')

def upload_s3(requet):
    return HttpResponse(json.dumps([1,2,3]), content_type='application/json')
