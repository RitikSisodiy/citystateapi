from django.db import models
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Country, city, cityLocations, state
# Create your views here.
def index(request):
    return render(request,"index.html")


def filtermodel(data,sample,resfieldcsv,modelname):
    if sample is not None:
        country = modelname.objects.values()[0]
        return [country]
    for f in modelname._meta.fields:
        if "ForeignKey" in str(type(f)):
            if data.get(f.name+"__iexact") is not None: 
                data[f.name] = data[f.name+"__iexact"]
                data.pop(f.name+"__iexact")
    pagesize = data.get('pagesize__iexact') if data.get('pagesize__iexact') is not None else 1000
    if data.get('pagesize__iexact') is not None: data.pop('pagesize__iexact')
    try:
        del data['data__iexact']
    except:
        pass
    arg =resfieldcsv.split(',') if resfieldcsv is not None else []
    print(data)
    print(arg)
    return modelname.objects.filter(**data).order_by('name')[:int(pagesize)].values(*arg)


def stateView(request):
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key+"__iexact":request.GET[key] for key in request.GET}
    data = filtermodel(data,sample,resval,state)
    return JsonResponse(list(data),safe=False)
def cityView(request):
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key+"__iexact":request.GET[key] for key in request.GET}
    data = filtermodel(data,sample,resval,city)
    return JsonResponse(list(data),safe=False)
def countryView(request):
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key+"__iexact":request.GET[key] for key in request.GET}
    data  = filtermodel(data,sample,resval,Country)
    return JsonResponse(list(data),safe=False)
def locationsView(request):
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key+"__iexact":request.GET[key] for key in request.GET}
    data = filtermodel(data,sample,resval,cityLocations)
    return JsonResponse(list(data),safe=False)