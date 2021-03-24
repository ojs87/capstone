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
    item= serialize('json', TarkovItemQuest.objects.filter(tarkovitem=TarkovItem.objects.filter(name=body)[0]))
    # item2 = serialize('json', quest)
    # return JsonResponse({"message" : body, "quest" : quest[0]})
    return JsonResponse({"message" : item})

def questroute(request):
    pass
