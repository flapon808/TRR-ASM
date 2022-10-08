from django.shortcuts import render
def index(request):
    return render(request,"index.html")

def weekly(request):
    return render(request,"weekly_offers.html")


