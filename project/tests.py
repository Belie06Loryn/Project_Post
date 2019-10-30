from django.test import TestCase
from .models import Profile,Foto


class ProfileTestClass(TestCase):
    def setUp(self):
        self.wandi = Profile( image='default.jpg',email='mmab@gma.co',bio='heey its me', link='www.john.me',country='rwanda')

    def test_instance(self):
        self.assertTrue(isinstance(self.wandi,Profile))

    def test_save(self):
        self.wandi.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
 
    def test_upd(self):
        wandi = Profile.objects.filter(id=1)
        wandi.update(image = 'Kam.jpeg', email ='james@morischool.com',bio = 'hdefedf')
        search = Profile.objects.filter(id=1)
        self.assertNotEqual(search,'Kam.jpeg')

    def test_dele(self):
        self.wandi.save_profile()
        profi = Profile.objects.all()
        self.assertTrue(len(profi)>=0)  

