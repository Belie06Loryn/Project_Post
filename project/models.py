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

class Foto(models.Model):
    image = models.ImageField(upload_to = 'photos/',null=True)
    sitename = models.CharField(max_length =40)
    url = models.CharField(max_length =40)
    description = models.CharField(max_length =6000)
    category = models.CharField(max_length =6000)
    tags = models.CharField(max_length =6000)
    technology = models.CharField(max_length =6000)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    designer = models.CharField(max_length =6000)
    author = models.CharField(max_length =6000)
     
    def save_pic(self):
        self.save()

    def dele_pic(self):
        self.delete() 

    @classmethod
    def image_by_id(cls,id):
        found = cls.objects.filter(id = id)
        return found

    @classmethod
    def update_pic(cls,id):
        imaje = cls.objects.filter(id=id).update(id=id)
        return imaje          
