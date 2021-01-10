from django.shortcuts import render, redirect
#from django.http import Http404
#from rest_framework import status
#from rest_framework.views import APIView
#from rest_framework.response import Response
from .serializers import MemberSerializer
from Member.models import Member
from rest_framework import generics

def index(request):
    return render(request, 'index.html', {})


def signin(request):
    return render(request, 'login.html', {})



class MemberList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer



"""

class Memberlist(APIView):

    def get(self, request, format=None):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Memberdetail(APIView):

    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        member = self.net_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)

    def put(self, request, pk, format=None) :
        member = self.get_object(pk)
        serializer = MemberSerializer(member, data=request.data)
        if serializer.isvaild():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, pk, format=None):
        member = self.net_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    #serializer = MemberSerializer()
    #serializer = JSONRenderer().render(serializer.data)
    #return HttpResponse(repr(serializer))


"""
