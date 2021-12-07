from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Country
# Create your views here.
def stateView(request):
    return HttpResponse('state')
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
        