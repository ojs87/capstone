from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class TarkovQuest(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default="")
    objectives = models.JSONField(default=dict)
    rewards = models.TextField(default="")
    questgiver = models.CharField(max_length=128)
    prereqs = models.JSONField(default=dict)
    leadsto = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class TarkovHideout(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class TarkovItem(models.Model):
    name = models.CharField(max_length=128)
    firquest = models.ManyToManyField(TarkovQuest, through='TarkovItemQuest')
    hideout = models.ManyToManyField(TarkovHideout, through="TarkovItemHideout")

    def __str__(self):
        return self.name

class TarkovItemQuest(models.Model):
    tarkovitem = models.ForeignKey(TarkovItem, on_delete=models.CASCADE)
    tarkovquest = models.ForeignKey(TarkovQuest, on_delete=models.CASCADE)
    numberofitems = models.IntegerField()
    foundinraid = models.BooleanField(default=False)


class TarkovItemHideout(models.Model):
    tarkovitem = models.ForeignKey(TarkovItem, on_delete=models.CASCADE)
    tarkovhideout = models.ForeignKey(TarkovHideout, on_delete=models.CASCADE)
    level1itemcount = models.IntegerField(blank=True)
    level2itemcount = models.IntegerField(blank=True)
    level3itemcount = models.IntegerField(blank=True)
    craftingreqs = models.JSONField(blank=True)
    stationlevel = models.IntegerField()
