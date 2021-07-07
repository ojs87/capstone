from django.contrib.auth.models import AbstractUser
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class User(AbstractUser):
    onquests = models.ManyToManyField("TarkovQuestTester", related_name="onquest")
    completedquests = models.ManyToManyField("TarkovQuestTester", related_name="completed")


class TarkovHideout(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class TarkovItem(models.Model):
    name = models.CharField(max_length=128)
    hideout = models.ManyToManyField(TarkovHideout, through="TarkovItemHideout")

    def __str__(self):
        return self.name


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
    slug = models.CharField(max_length=128)
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

class TarkovQuestStructure(MPTTModel):
    name=models.CharField(max_length=50, unique=True)
    questgiver = models.CharField(max_length=50, default="Prapor")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class TarkovFoundInRaid(models.Model):
    name = models.CharField(max_length=128)
    canbecrafted = models.CharField(max_length=128)
    questreward = models.CharField(max_length=128)
    kappa = models.CharField(max_length=128)
    amount = models.IntegerField()
    quest = models.ForeignKey(TarkovQuestTester, on_delete=models.CASCADE)

    @classmethod
    def create(cls, **kwargs):
        quest= cls.objects.create(
            name=kwargs['name'],
            canbecrafted=kwargs['canbecrafted'],
            questreward=kwargs['questreward'],
            kappa=kwargs['kappa'],
            amount=kwargs['amount'],
            quest=TarkovQuestTester.objects.get(name=kwargs['quest'])
        )
        return quest

    def __str__(self):
        return self.name
