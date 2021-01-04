from django.db import models

class Member(models.Model):
    member_uid = models.SmallIntegerField(primary_key=True)
    account = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    auth = models.BooleanField()  #  지워
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

#    class Meta:
 #       ordering = ['created']