from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from FoodApp.forms import ItemForm
from .models import Item
from django.template import loader


# Create your views here.
def index(request):
    #return HttpResponse("<h1>HELLO DJANGO</h1>")
    item_list = Item.objects.all()
    
    context = {
        'item_list' : item_list,
    }
    return render(request,'FoodApp/index.html', context)

#Details View Function - FoodApp\1 
def detailview(request, item_id):
    item = Item.objects.get(pk = item_id)
    context = {
        'item':item,
    }
    return render(request, 'FoodApp/detail.html', context)

#Details View of Example - FoodApp/1
'''def detailview(request, item_id):
    return HttpResponse("This is Item No\Id: %s" % item_id)'''

#Create Form to add Items
#ADD NEW ITEM 
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        #after saving redirect to home page 
        return redirect("/FoodApp/")
    return render(request, 'FoodApp/item-form.html', {'form':form})

#Code for Update Item - Forms.py
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect("/FoodApp/")
    return render(request, 'FoodApp/item-form.html', {'form':form, 'item':item})

#Code for Delete Item
def delete_item(request,id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect("/FoodApp/")
    return render(request, 'FoodApp/item-delete.html', {'item':item})