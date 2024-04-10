from django.shortcuts import render
from django.http import HttpResponse
from website.models import BasicInformationModel, SkillModel, PhotoModel
    


def index(request):
    BasicInfo = BasicInformationModel.objects.first()
    Skills = SkillModel.objects.all()
    gallery = PhotoModel.objects.all()
    context ={
        'BasicInfo':BasicInfo,
        'Skills': Skills,
        'gallery':gallery,
        }
    return render(request, "website/index.html", context)

def about(request):
    return render(request, "website/about.html")

def contact(request):
    return render(request, "website/contact.html")
    
    