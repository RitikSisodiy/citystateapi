from django.db import models
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Country, city, cityLocations, state
# Create your views here.
def filtermodel(data,sample,resfieldcsv,modelname):
    if sample is not None:
        country = modelname.objects.values()[0]
        return JsonResponse(country,safe=False)
    try:
        del data['data']
    except:
        pass
    arg =resfieldcsv.split(',') if resfieldcsv is not None else []
    print(data)
    print(arg)
    return modelname.objects.filter(**data).values(*arg)


def stateView(request):
    country = request.GET.get('countryid')
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key:request.GET[key] for key in request.GET}
    if sample is not None:
        statedata = state.objects.values()[0]
        return JsonResponse(statedata,safe=False)
    if country is not None :
        try:
            del data['countryid']
            del data['data']
        except:
            pass
        data['country'] = country
        arg =resval.split(',') if resval is not None else []
        print(data)
        print(arg)
        country  = state.objects.filter(**data).values(*arg).order_by('name')
        return JsonResponse(list(country),safe=False)
    return HttpResponse('country is required',status=404)
def cityView(request):
    State = request.GET.get('stateid')
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key+"__iexact":request.GET[key] for key in request.GET}
    if sample is not None:
        statedata = city.objects.values()[0]
        return JsonResponse(statedata,safe=False)
    if State is not None :
        try:
            del data['stateid__iexact']
            del data['data__iexact']
        except:
            pass
        data['state'] = State
        arg =resval.split(',') if resval is not None else []
        print(data)
        print(arg)
        country  = city.objects.filter(**data).values(*arg).order_by('name')
        return JsonResponse(list(country),safe=False)
    return HttpResponse('stateid is required',status=404)
def countryView(request):
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key:request.GET[key] for key in request.GET}
    data  = filtermodel(data,sample,resval,Country)
    return JsonResponse(list(data),safe=False)
def locationsView(request):
    State = request.GET.get('cityid')
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key:request.GET[key] for key in request.GET}
    if sample is not None:
        statedata = cityLocations.objects.values()[0]
        return JsonResponse(statedata,safe=False)
    if State is not None :
        try:
            del data['cityid']
            del data['data']
        except:
            pass
        data['city'] = State
        arg =resval.split(',') if resval is not None else []
        print(data)
        print(arg)
        country  = cityLocations.objects.filter(**data).values(*arg).order_by('name')
        return JsonResponse(list(country),safe=False)
    return HttpResponse('country is required',status=404)