from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Job,Jobseeker

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        write_only=True,
        min_length=8
    )
    class Meta:
        model=User,
        fields=['id','username','email','password']

class JobSerializer(serializers.ModelSerializer):
    posted_by=serializers.ReadOnlyField(
        source='posted_by.username'
    )
    class Meta:
        model=Job
        fields='__all__'
        read_only_fields=['id','create_at','posted_by']

class JobseekerSerializer(serializers.ModelSerializer):
    applicant=serializers.ReadOnlyField(
        source='applicant.username'
    )
    class Meta:
        model=Jobseeker
        fields='__all__'
        read_only_fields=['id','applicant','applied_at']