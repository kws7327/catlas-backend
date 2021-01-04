from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import MemberSerializer
from Member.models import Member


def index(request):
    return render(request, 'index.html', {})


def signin(request):
    return render(request, 'login.html', {})

@api_view(['GET','POST'])

def Member_list(request):

    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Member_detail(request, pk):

    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MemberSerializer(member, data=data)
        if serializer.isvaild():
            serializer.save()
            return JsonResponse()
        return JsonResponse(serializer.errors, status=400)
            
    elif request.method == 'DELETE':
        member.delete()
        return HttpResponse(status=204)
        

    #serializer = MemberSerializer()
    #serializer = JSONRenderer().render(serializer.data)
    #return HttpResponse(repr(serializer))



