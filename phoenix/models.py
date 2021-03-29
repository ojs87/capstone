from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class TarkovQuest(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default="", blank=True)
    objectives = models.JSONField(default=dict, blank=True)
    rewards = models.JSONField(default=dict, blank=True)
    questgiver = models.CharField(max_length=128, blank=True)
    prereqs = models.JSONField(default=dict, blank=True)
    leadsto = models.JSONField(default=dict, blank=True)

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
    foundinraid = models.BooleanField(default=True)


class TarkovItemHideout(models.Model):
    tarkovitem = models.ForeignKey(TarkovItem, on_delete=models.CASCADE)
    tarkovhideout = models.ForeignKey(TarkovHideout, on_delete=models.CASCADE)
    level1itemcount = models.IntegerField(blank=True)
    level2itemcount = models.IntegerField(blank=True)
    level3itemcount = models.IntegerField(blank=True)
    craftingreqs = models.JSONField(blank=True)
    stationlevel = models.IntegerField()

class TarkovQuestTester(models.Model):
    name = models.CharField(max_length=128)
    questhref = models.URLField(blank=True)
    objectives = models.JSONField(default=dict, blank=True)
    rewards = models.JSONField(default=dict, blank=True)
    requirements = models.JSONField(default=dict, blank=True)
    questgiver = models.CharField(max_length=128, blank=True)
    prereqs = models.JSONField(default=dict, blank=True)
    leadsto = models.JSONField(default=dict, blank=True)

    @classmethod
    def create(cls, **kwargs):
        quest= cls.objects.create(
            name=kwargs['quest'],
            questhref=kwargs['quest-href'],
            objectives=kwargs['objectives'],
            rewards=kwargs['rewards'],
            requirements=kwargs['requirements'],
            questgiver=kwargs['questgiver'],
            prereqs=kwargs['prereqs'],
            leadsto=kwargs['leadsto']
        )
        return quest
        
    def __str__(self):
        return self.name
