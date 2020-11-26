from django.shortcuts import render, redirect
from rest_framework.renderers import JSONRenderer
from .serializers import MemberSerializer
from django.http import HttpResponse


def index(request):
    return render(request,'index.html', {})

def signin(request):
    return render(request, 'login.html', {})




    #serializer = MemberSerializer()
    #serializer = JSONRenderer().render(serializer.data)
    #return HttpResponse(repr(serializer))



