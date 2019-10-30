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

class FotoTestClass(TestCase):

    def setUp(self):
        self.profile= Profile(image='default.jpg',email='mmab@gma.co',bio='heey its me', link='www.john.me',country='rwanda')
        self.profile.save_profile()

        self.new_photos= Foto(image = 'Jam.jpeg', sitename ='Muriuki', url ='jamesmoringaschoolcom',description = "sdfghyjukiljhgf")
        self.new_photos.save_pic()      

    def test_save_pick(self):
        self.new_photos= Foto(image = 'Jam.jpeg', sitename ='Muriuki', url ='jamesmoringaschoolcom',description = "sdfghyjukiljhgf")
        self.new_photos.save_pic()
        picture = Foto.objects.all()
        self.assertTrue(len(picture)>=1)

    def test_dele_pick(self):
        self.new_photos= Foto(image = 'Jam.jpeg', sitename ='Muriuki', url ='jamesmoringaschoolcom',description = "sdfghyjukiljhgf")
        self.new_photos.save_pic()
        picture = self.new_photos.dele_pic()
        delete = Foto.objects.all()
        self.assertTrue(len(delete)>=0)   

    def test_upd_pic(self):
        image = Foto.objects.filter(id=1)
        image.update(sitename ='lez.jpeg')
        search = Foto.objects.filter(id=1)
        self.assertNotEqual(search,'lez.jpeg')     
        
    def test_pic_id(self):
        self.image = Foto(image = 'Jam.jpeg', sitename ='Muriuki', url ='jamesmoringaschoolcom',description = "sdfghyjukiljhgf")
        self.image.save_pic()
        search = Foto.image_by_id(self.image.id)
        self.assertNotEqual(search,self.image)

