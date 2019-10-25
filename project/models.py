from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    image = models.ImageField(upload_to = 'profiles/',null=True)
    username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length =40,null=True)
    bio = models.CharField(max_length =6000)
    link = models.CharField(max_length =6000)
    country = models.CharField(max_length =6000)
    linked = models.CharField(max_length =6000)
    instagram = models.CharField(max_length =6000)

    def save_profile(self):
        self.save()

    def dele_profile(self):
        self.delete() 

    @classmethod
    def update_profile(cls,id,bio):
        profile = cls.objects.filter(id=id).update(bio=bio)
        return profile  

    @classmethod
    def profile_by_id(cls,id):
        found = cls.objects.filter(id = id)
        return found       

    @classmethod
    def find_profile(cls,search):
        found = cls.objects.filter(username__username__icontains=search)
        return found
    
    def __str__(self):
        return self.bio   