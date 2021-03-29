import json, csv
from django.shortcuts import render
from django.http import HttpResponse
from .models import TarkovItem, TarkovQuest, TarkovItemQuest, TarkovQuestTester
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
    quests= TarkovQuestTester.objects.all()
    prapor=quests.filter(questgiver='Prapor').order_by("name")
    therapist=quests.filter(questgiver='Therapist').order_by("name")
    fence=quests.filter(questgiver='Fence').order_by("name")
    skier=quests.filter(questgiver='Skier').order_by("name")
    peacekeeper=quests.filter(questgiver='Peacekeeper').order_by("name")
    mechanic=quests.filter(questgiver='Mechanic').order_by("name")
    ragman=quests.filter(questgiver='Ragman').order_by("name")
    jaeger=quests.filter(questgiver='Jaeger').order_by("name")
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
    x=TarkovQuestTester.objects.get(name=quest)

    # rewards=str(x.rewards)
    # rewards1=rewards.replace("\\n", "<ul><li>", 1)
    # rewards2=rewards1.replace("\\n", "<li>", 1)
    # rewards3=rewards2.replace("Center Level 2", "Center Level 2</ul>", 1)
    # rewards4=rewards3.replace("'", '"')
    # rewards5 = json.loads(rewards4)
    # x.rewards=rewards5
    #
    # objectives=str(x.objectives)
    # if "(Optional)" in objectives:
    #     objectives1=objectives.replace("\\n", "<ul><li>", 1)
    #     objectives2=objectives1.replace("\\n", "</li><li>", 1)
    # #     objectives3=objectives2.replace("'", '"')
    # #     # objectives3 = json.loads(objectives2)
    # #     x.objectives=objectives2

    return render(request, 'phoenix/quests.html',{
        "quest" : x
    })

def importjson():
    with open('phoenix/csvjson(1).json', encoding='utf-8') as data_file:
        json_data = json.loads(data_file.read())

        for quest_data in json_data:
            movie = TarkovQuestTester.create(**quest_data)
