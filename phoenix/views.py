import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import TarkovItem, TarkovQuest, TarkovItemQuest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

def index(request):
    return render(request, 'phoenix/index.html',{
    })

def items(request):
    items=TarkovItem.objects.all()
    quests=TarkovQuest.objects.all()
    itemquest=TarkovItemQuest.objects.all()
    return render(request, 'phoenix/items.html', {
        "items" : items,
        "quests" : quests,
        "itemquest" : itemquest
    })

@csrf_exempt
def itemroute(request):
    data=json.loads(request.body)
    body=data.get("body", "")
    itemquest = TarkovItemQuest.objects.filter(tarkovitem=TarkovItem.objects.get(name=body))
    # quest = itemquest[0]
    # quest2 = str(quest.tarkovquest)
    quest2={}
    y=0
    num="numberofitems"
    for x in itemquest:
        quest2[y] = {"quest" : str(x.tarkovquest), "num" : str(x.numberofitems)}
        
        y=y+1
    # item= serialize('json', quest)
    # item2 = serialize('json', quest)
    # return JsonResponse({"message" : body, "quest" : quest[0]})
    return JsonResponse(quest2)

def questroute(request):
    pass
