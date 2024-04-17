from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
# Create your models here.

MEMBER_CHOICES = [
    ("Speaker", "Speaker"),
    ("Participant", "Participant"),
]

class ConferenceModel(models.Model):
    conference_title = models.TextField(null=False,primary_key=True)
    conference_description = models.CharField(max_length=1000,null=False)
    conference_start_date = models.DateField(null=False)
    conference_end_date = models.DateField(null=False)

class TalkModel(models.Model):
    talk_conference_title  = models.ForeignKey(ConferenceModel,on_delete=models.CASCADE)
    talk_title = models.TextField(null=False,primary_key=True)
    talk_description =  models.CharField(max_length=100,null=False)
    talk_duration = models.DecimalField(max_digits=2,decimal_places=1)
    talk_time = models.TimeField(null=True)

class MemberModel(models.Model):
    member_talk_title = models.ForeignKey(TalkModel,on_delete=models.CASCADE)
    member_type = models.CharField(max_length=25,null=False,choices=MEMBER_CHOICES)
    member_name = models.TextField(primary_key=True,null=False)
    member_email = models.EmailField(max_length=100,null=False,unique=True)