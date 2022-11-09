from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import JsonResponse
from .models import Category, Cuisine, Menu_Item

# Create your views here.
def index(request):
    return HttpResponse("Hello, you shouldn't be here")

def get_menu(request):
    # ## data = list(Menu_Item.objects.values('category__title'))
    # data = list(Menu_Item.objects.values())
    # return JsonResponse({'data' : data})
    categories = Category.objects.values()
    cuisines = Cuisine.objects.values()
    print(cuisines)
    menu = Menu_Item.objects.values()
    print(menu)
    data = []
    print(categories[0]['title'])
    print(cuisines[0])
    index = 0
    for item in menu:
        item['category_id'] = categories[item['category_id'] - 1]
        item['cuisine_id'] = cuisines[item['cuisine_id'] - 1]
        data.append(item)
    return JsonResponse({'data': data})
    # for item in menu:
    #     setattr(item, 'category_id', getattr(ca, name))
    

def cuisine_get(request, cuisine_id):
    return HttpResponse("You're looking at cuisine %s." %cuisine_id)

def some_view(request):
    data = list(SomeModel.objects.values())  # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})