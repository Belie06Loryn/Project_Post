from .models import Profile,Foto
from django import forms
        
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image','username','email','bio','link','country','linked','instagram'] 

class FotoForm(forms.ModelForm):
  class Meta:
    model = Foto
    fields = ['image','sitename','url','description','category','tags','technology','profile','designer','author'] 