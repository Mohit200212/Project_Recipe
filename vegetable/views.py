from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return render(request, "Index.html")




    peoples=[
        
            {'name':'Mohit Gautam','age':22},
            {'name':'Rohit Gautam', 'age':23},
            {'name':'Rajput Gautam', 'age':25},
            {'name':'Rakesh Patle', 'age':26},
            {'name':'Rohit Bhure', 'age':27},
            {'name':'Neeraj Kumar', 'age':15},
            {'name':'Rakesh Patle', 'age':16},
            {'name':'Rohit Bhure', 'age':17},
            {'name':'Neeraj Kumar', 'age':28},
            {'name':'Lalit Kumar', 'age':17},

        
    ]

    for people in peoples:
        print(people)

    return render(request,"Index.html", context={'peoples':peoples})





