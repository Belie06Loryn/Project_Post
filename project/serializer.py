from rest_framework import serializers
from .models import Profile,Foto


class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ('image','username','email','bio','link','country','linked','instagram') 

class FotoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Foto
    fields = ('image','sitename','url','description','technology','profile','profiles','author') 
