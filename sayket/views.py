from django.shortcuts import render

# Create your views here.
from  django.shortcuts import render
from django.http import JsonResponse
from .models import District,Division,Category



def  search (request):

    return render (request, template_name='index.html')


def data(request):
    context = {
        'Division': list(Division.objects.values()),

        'Category': list(Category.objects.values()),


    }
    return JsonResponse(context, safe=False)


def district (request):
    print(request.GET)
    query = District.objects
    if request.GET.get('division'):
        query = query.filter(division=request.GET.get('division'))

    context = {

        'District': list(query.values()),


    }
    return JsonResponse(context, safe=False)




