from django.shortcuts import render
from django.http import HttpResponse
from .models import Logistics

# Create your views here.
def LogisticsIndex(request):
    #HttpResponse
    #return HttpResponse("WELCOME TO LOGISTICS")
    logistics_list = Logistics.objects.all()
    context = {
        'logistics_list' : logistics_list,
    }
    return render(request, 'LogisticsApp/Logistics.html', context)


#Details View Function - LogisticsApp\1 
def logisticsdetailview(request, Request_No):
    logistics = Logistics.objects.get(pk = Request_No)
    context = {
        'logistics':logistics,
    }
    return render(request, 'LogisticsApp/Logisticsdetail.html', context)




