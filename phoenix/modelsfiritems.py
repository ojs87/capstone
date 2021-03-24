# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TarkovItems

class FirItems(models.Model):
    name = models.TextField(blank=True, primary_key=True)
    fir_status = models.BooleanField(blank=True, null=True)
    quest1 = models.IntegerField(blank=True, null=True)
    quest2 = models.IntegerField(blank=True, null=True)
    hideout = models.IntegerField(blank=True, null=True)
    mycount = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'fir_items'
