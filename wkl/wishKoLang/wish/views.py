from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def welcome(request):
    return render(request, "wish/subpages/Initials/welcome.html")

def login(request):
    return render(request, "wish/subpages/Initials/login.html")

def signup(request):
    return render(request, "wish/subpages/Initials/signup.html")

def setup(request):
    return render(request, "wish/subpages/Initials/setup.html")

def home(request):
    return render(request, "wish/pages/home.html")

def openGifting(request):
    return render(request, "wish/pages/openGifting.html")

def organization(request):
    return render(request, "wish/subpages/OpenGifting/organization.html")

def secretSanta(request):
    return render(request, "wish/pages/secretSanta.html")

def createGroup(request):
    return render(request, "wish/subpages/SecretSanta/createGroup.html")

def group(request):
    return render(request, "wish/subpages/SecretSanta/group.html")

def runRoulette(request):
    return render(request, "wish/subpages/SecretSanta/runRoulette.html")

def friends(request):
    return render(request, "wish/pages/friends.html");