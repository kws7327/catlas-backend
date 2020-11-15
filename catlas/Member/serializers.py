from rest_framework.serializers import ModelSerializer
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    #model = Member
    #fields = ('member_uid','account','password','auth','name','email')
    #member_uid = models.SmallIntegerField(primary_key=True)
    #account = models.CharField(max_length=50)
    #auth = models.BooleanField()
    #name = models.CharField(max_length=50)
    #email = models.CharField(max_length=50)