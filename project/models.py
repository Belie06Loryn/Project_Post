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
    technology = models.CharField(max_length =6000)
    profiles = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
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
 
    @classmethod
    def searchs(cls,search):
        sitename = cls.objects.filter(sitename__icontains=search)
        return sitename 

class Voting(models.Model):
    design = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    usability = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    content = models.IntegerField(choices=[(i,i) for i in range(1,11)])
    project = models.ForeignKey(Foto,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return f'{self.user.username} {self.project.sitename} Rating'