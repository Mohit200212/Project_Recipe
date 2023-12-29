from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages



# Create your views here.
def Recipes(request):
    if request.method=="POST":
        data=request.POST
        Recipe_name=data.get("Recipe_name")
        Recipe_discription=data.get("Recipe_discription")
        Recipe_image=request.FILES.get("Recipe_image")
        print(Recipe_name)
        print(Recipe_discription)
        print(Recipe_image)
        messages.success(request,"Recipes Added Successfully")

        Recipe.objects.create(
            Recipe_name=Recipe_name,
            Recipe_discription=Recipe_discription,
            Recipe_image=Recipe_image,
        )

        
        # return HttpResponseRedirect('/Recipes/')
        

        return render(request, "Recipes.html")
    
    # if request.GET.get("search"):
    #         queryset=queryset.filter(Recipe_name__contains=request.GET.get("search"))
    #         queryset=Recipe.objects.all()
    #         context={'Recipe':queryset}
    return render(request, "Recipes.html")





def ShowData(request):
    queryset=Recipe.objects.all()
    context={'Recipe':queryset}
    return render(request,"showdata.html", context)

def DeleteRecipe(request,id):
    
    queryset=Recipe.objects.get(pk=id)
    queryset.delete()
    messages.success(request,"Recipes Deleted Successfully")

    return redirect("showdata")

def UpdateRecipe(request, id):
    queryset=Recipe.objects.get(pk=id)
    if request.method=="POST":
        data=request.POST
        Recipe_name=data.get("Recipe_name")
        Recipe_discription=data.get("Recipe_discription")
        Recipe_image=request.FILES.get("Recipe_image")

        queryset.Recipe_name=Recipe_name
        queryset.Recipe_discription=Recipe_discription

        if Recipe_image:
            queryset.Recipe_image=Recipe_image
        
        queryset.save()
        messages.success(request,"Recipes Upadated Successfully")

        return redirect("showdata")
        

  
    context={'Recipe':queryset}

    return render(request, "Update_Recipes.html",context)





