from rest_framework.serializers import ModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('member_uid','account','password','auth','name','email')

#serializer = MemberSerializer()
#serializer = JSONRenderer().render(serializer.data)

