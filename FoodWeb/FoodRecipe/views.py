from django.shortcuts import render
from django.http import HttpResponse

import json
# Create your views here.
import pandas as pd
from .models import Fooditems
def index(request):
    return HttpResponse("Food Recipe Index Page")

def recipepage(request):
    return render(request,'FoodRecipe/Recipe.html')
def showrecipe(request):
    if(request.method=="POST"):

        foodname = request.POST.get("foodname")
        foodname = foodname.strip().lower()
        fooditem = Fooditems.objects.filter(name=foodname)

        if(fooditem.exists()):
            fooditem = fooditem[0]
            ingredients = fooditem.ingredients

            steps = fooditem.steps
            valdict = {'name':fooditem.name,'ingredients':ingredients,'steps':steps}
            return render(request,'FoodRecipe/showrecipepage.html',valdict)

        else:
            return HttpResponse("<h1>Food not found</h1>")

    else:
        return HttpResponse("<h1>Error</h1>")



'''
TO ADD Data
# file = pd.read_csv('FoodRecipe/FoodRecipefile.csv')
#         # file.reset_index(inplace=True)
#         model = Fooditems()
#         print(file.shape)
#         for i in range(file.shape[0]):
#             print(i)
#             file['steps'][i] = json.loads(file['steps'][i])
#             file['ingredients'][i] = json.loads(file['ingredients'][i])
#             food  = Fooditems(i,file['name'][i],file['minutes'][i],file['n_steps'][i],file['steps'][i],file['ingredients'][i],file['n_ingredients'][i])
# 
#             food.save()
'''