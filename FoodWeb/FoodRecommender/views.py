from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from FoodRecipe.models import Fooditems


def get_score(user_item,item):

    ui = set(user_item)
    i = set(item)
    anditem = ui & i
    oritem = ui | i
    return len(anditem)/len(oritem)

def get_top_nmatch(user_item,items,n=1):
    score_list = []
    for id,item in items:
        score = get_score(user_item,item)
        if(score!=0):
            score_list.append([score,id])

    score_list.sort(reverse=True)
    score_list = score_list[:min(n,len(score_list))]
    return list(map(lambda x: x[1],score_list) )


def get_recommendation(request):
    if (request.method == "POST"):
        user_item = request.POST.get('foodname')
        print("*"*50)
        print(request.POST)


        user_item = user_item.strip()
        user_item = user_item.split(',')
        user_item = list(map(lambda x:x.strip(' /,\'\" ').lower(),user_item))
        print(user_item)
        allfood = Fooditems.objects.all()
        items = []
        for food in allfood:
            ing = food.ingredients
            id = food.foodid
            items.append([id,ing])
        top_ids = get_top_nmatch(user_item,items,3)
        print(top_ids)
        top_food_items = []
        for id in top_ids:
            fooditem = Fooditems.objects.filter(foodid=id)[0]

            valdict = {'name': fooditem.name, 'ingredients': fooditem.ingredients, 'steps': fooditem.steps}
            top_food_items.append(valdict)

        return render(request,'FoodRecommender/recommender_result.html',{'food_items':top_food_items})
    else:
        return HttpResponse("<h1>Error POST Request require</h1>")


def recommendation_home(request):
    return render(request, 'FoodRecommender/recommender.html')
