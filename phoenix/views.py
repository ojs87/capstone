import json, csv
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import TarkovItem, TarkovQuest, TarkovItemQuest, TarkovQuestTester, TarkovFoundInRaid, TarkovQuestStructure
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError



def index(request):
    return render(request, 'phoenix/index.html',{
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "phoenix/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "phoenix/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "phoenix/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "phoenix/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "phoenix/register.html")

def foundinraid(request):
    items=TarkovFoundInRaid.objects.all().values('name').distinct().order_by('name')
    quests=TarkovQuest.objects.all()
    itemquest=TarkovItemQuest.objects.all()
    return render(request, 'phoenix/foundinraid.html', {
        "items" : items,
        "quests" : quests,
        "itemquest" : itemquest
    })

def items(request):
    return render(request, 'phoenix/items.html')

def tracker(request):
    # a=TarkovQuestTester.objects.all()
    # b=TarkovQuestStructure.objects.create(name=x.name)
    # for x in b:
    #     c=TarkovQuestTester.objects.get(name=x.name)
    #     for d in c.prereqs:
    #         e=TarkovQuestTester.objects.get(name=d['prereqs'])
    #         x.save(parent=e)
    return render(request, "phoenix/tracker.html", {
        'quests' : TarkovQuestStructure.objects.all()
    })


@csrf_exempt
def itemroute2(request):
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

@csrf_exempt
def itemroute(request):
    data=json.loads(request.body)
    body=data.get("body", "")
    itemquest=TarkovFoundInRaid.objects.filter(name=body)

    quest2={}
    y=0
    num="numberofitems"
    for x in itemquest:
        quest2[y] = {"quest" : str(x.quest), "num" : str(x.amount)}
        y+=1

    return JsonResponse(quest2)

def questroute(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        nodedata=data.get("node", "")
        childdata=data.get("childnode", "")
        firstuff=TarkovFoundInRaid.objects.filter(quest=TarkovQuestTester.objects.get(name=nodedata).id)
        jsonstuff = {}
        y=0
        for x in firstuff:
            jsonstuff[y] = {"quest" : str(x.quest), "item" : str(x.name), "num" : str(x.amount)}
            y+=1
        for x in childdata:
             p=TarkovFoundInRaid.objects.filter(quest=TarkovQuestTester.objects.get(name=x).id)
             for i in p:
                 jsonstuff[y] = {"quest" : str(i.quest), "item" : str(i.name), "num" : str(i.amount)}
                 y+=1
        response = JsonResponse(jsonstuff)
        return response

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
        praporjson.update({y : { 0: prapor[y].slug, 1: prapor[y].name}})
        y+=1

    y=0
    for x in therapist:
        therapistjson.update({y : { 0: therapist[y].slug, 1: therapist[y].name}})
        y+=1

    y=0
    for x in fence:
        fencejson.update({y : { 0: fence[y].slug, 1: fence[y].name}})
        y+=1

    y=0
    for x in skier:
        skierjson.update({y : { 0: skier[y].slug, 1: skier[y].name}})
        y+=1

    y=0
    for x in peacekeeper:
        peacekeeperjson.update({y : { 0: peacekeeper[y].slug, 1: peacekeeper[y].name}})
        y+=1

    y=0
    for x in mechanic:
        mechanicjson.update({y : { 0: mechanic[y].slug, 1: mechanic[y].name}})
        y+=1

    y=0
    for x in ragman:
        ragmanjson.update({y : { 0: ragman[y].slug, 1: ragman[y].name}})
        y+=1

    y=0
    for x in jaeger:
        jaegerjson.update({y : { 0: jaeger[y].slug, 1: jaeger[y].name}})
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
    x=TarkovQuestTester.objects.get(slug=quest)
    prereqs= {}
    leadsto = {}

    for prereq in x.prereqs:
        prereqs.update({TarkovQuestTester.objects.get(name=prereq["prereqs"]).name : TarkovQuestTester.objects.get(name=prereq["prereqs"]).slug})

    for leadto in x.leadsto:
        leadsto.update({TarkovQuestTester.objects.get(name=leadto["leadsto"]).name : TarkovQuestTester.objects.get(name=leadto["leadsto"]).slug})

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
        "quest" : x,
        "prereqs" : prereqs,
        "leadsto" : leadsto,
    })

def importjson():
    with open('phoenix/csvjson(2).json', encoding='utf-8') as data_file:
        json_data = json.loads(data_file.read())

        for quest_data in json_data:
            movie = TarkovFoundInRaid.create(**quest_data)
