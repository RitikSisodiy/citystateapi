from django.db import models
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Country, state
# Create your views here.
def stateView(request):
    country = request.GET.get('countryid')
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key:request.GET[key] for key in request.GET}
    if country is not None :
        try:
            del data['countryid']
            del data['data']
        except:
            pass
        data['country'] = country
        if sample is not None:
            statedata = state.objects.values()[0]
            return JsonResponse(statedata,safe=False)
        arg =resval.split(',') if resval is not None else []
        print(data)
        print(arg)
        country  = state.objects.filter(**data).values(*arg).order_by('name')
        return JsonResponse(list(country),safe=False)
    return HttpResponse('country is required',status=404)
def cityView(request):
    return HttpResponse('city')
def countryView(request):
    sample = request.GET.get('sample')
    resval = request.GET.get('data')
    data = {key:request.GET[key] for key in request.GET}
    try:
        del data['data']
    except:
        pass
    if sample is not None:
        country = Country.objects.values()[0]
        return JsonResponse(country,safe=False)
    arg =resval.split(',') if resval is not None else []
    print(data)
    print(arg)
    country  = Country.objects.filter(**data).values(*arg)
    return JsonResponse(list(country),safe=False)
        