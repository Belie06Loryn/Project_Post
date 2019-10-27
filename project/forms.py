from .models import Profile,Foto,Voting
from django import forms
        
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['image','username','email','bio','link','country','linked','instagram'] 

class FotoForm(forms.ModelForm):
  class Meta:
    model = Foto
    fields = ['image','sitename','url','description','technology','profile','profiles','author'] 

class VotingForm(forms.ModelForm):
  class Meta:
    model = Voting
    fields = ["design","usability","content"]    