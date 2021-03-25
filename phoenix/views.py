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

        y += 1
    # item= serialize('json', quest)
    # item2 = serialize('json', quest)
    # return JsonResponse({"message" : body, "quest" : quest[0]})
    return JsonResponse(quest2)

def questroute(request):
    quests= TarkovQuest.objects.all()
    prapor=quests.filter(questgiver='Prapor')
    therapist=quests.filter(questgiver='Therapist')
    fence=quests.filter(questgiver='Fence')
    skier=quests.filter(questgiver='Skier')
    peacekeeper=quests.filter(questgiver='Peacekeeper')
    mechanic=quests.filter(questgiver='Mechanic')
    ragman=quests.filter(questgiver='Ragman')
    jaeger=quests.filter(questgiver='Jaeger')
    jaegerjson = {}
    praporjson = {}
    therapistjson = {}
    fencejson = {}
    skierjson = {}
    peacekeeperjson = {}
    mechanicjson = {}
    ragmanjson = {}
    y=0
    for x in prapor:
        praporjson.update({y : prapor[y].name})
        y+=1

    y=0
    for x in therapist:
        therapistjson.update({y : therapist[y].name})
        y+=1

    y=0
    for x in fence:
        fencejson.update({y : fence[y].name})
        y+=1

    y=0
    for x in skier:
        skierjson.update({y : skier[y].name})
        y+=1

    y=0
    for x in peacekeeper:
        peacekeeperjson.update({y : peacekeeper[y].name})
        y+=1

    y=0
    for x in mechanic:
        mechanicjson.update({y : mechanic[y].name})
        y+=1

    y=0
    for x in ragman:
        ragmanjson.update({y : ragman[y].name})
        y+=1

    y=0
    for x in jaeger:
        jaegerjson.update({y : jaeger[y].name})
        y+=1

    questjson = {}
    questjson.update({"prapor" : praporjson})
    questjson.update({"therapist" : therapistjson})
    questjson.update({"fence" : fencejson})
    questjson.update({"skier" : skierjson})
    questjson.update({"peacekeeper" : peacekeeperjson})
    questjson.update({"mechanic" : mechanicjson})
    questjson.update({"ragman" : ragmanjson})
    questjson.update({"jaeger" : jaegerjson})


    return JsonResponse(questjson)

def quests(request, quest):
    return render(request, 'phoenix/index.html',{
    })
