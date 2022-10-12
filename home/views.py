from django.shortcuts import render
def index(request):
    return render(request,"index.html")

def weekly(request):
    return render(request,"weeklymeals.html")

def restaurants(request):
    return render(request,"showproducts.html")


     

