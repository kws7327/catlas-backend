from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ModelSerializer
from .models import Member

class MemberViewSet(viewsets.MemberViewSet):
    #queryset = Member.objects.all()
    #serializer_class = MemberSerializer