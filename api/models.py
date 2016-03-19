from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now


class Artboard(models.Model):
    title = models.CharField(max_length=1000)
    hash_tag = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)
    size_x = models.IntegerField(null=True)
    size_y = models.IntegerField(null=True)
    created_at = models.DateField(default=now)


class ArtboardOwnerRelation(models.Model):
    artboard_id = models.IntegerField(null=False)
    account_id = models.IntegerField(null=False)
    display_name = models.CharField(max_length=255)


class IngredientImages(models.Model):
    artboard_id = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)
    image_url = models.CharField(max_length=1000)
    posision_x = models.IntegerField(null=True)
    posision_y = models.IntegerField(null=True)
    created_at = models.DateField(default=now)
