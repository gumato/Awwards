from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'profile/')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    contacts=models.CharField(max_length=50, blank=True,default="contact")
    bio = models.CharField(max_length=100, blank=True,default="bio")

    class Meta:
        ordering=['-profile_photo']

    def __str__(self):
        return self.contacts

    def save_user(self):
        self.save()

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user_id=instance)

class Project(models.Model):
    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=800)
    link = models.CharField(max_length=60,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.description

    def save_project(self):
        self.save()

    def set_description(self,new_description):
        self.description = new_description
        self.save()
    
    @classmethod
    def search_by_name(cls,search_term):
        project = Project.objects.filter(title__icontains = search_term)
        return project

class Reviews(models.Model):

    RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    )
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name='reviews',null=True)
    design = models.IntegerField(choices=RATING_CHOICES,default=0)
    usability = models.IntegerField(choices=RATING_CHOICES,default=0)
    content = models.IntegerField(choices=RATING_CHOICES,default=0)
    comment = models.CharField(max_length=150,null=True)
    
    @classmethod
    def get_reviews(cls):
        reviews = Reviews.objects.all()
        return reviews     
