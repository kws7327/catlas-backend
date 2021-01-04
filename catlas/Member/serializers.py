from rest_framework.serializers import ModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['member_uid','account','password','auth','name','email']


    def create(self,validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.account = validated_data.get('account',instance.account)
        instance.password = validated_data.get('password',instance.password)
        instance.auth = validated_data.get('auth',instance.auth)
        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance

#serializer = MemberSerializer()
#serializer = JSONRenderer().render(serializer.data)