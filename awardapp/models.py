from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    bio = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to='profile/')
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name
    def save_profile(self):
        self.save()




class Project(models.Model):
    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=60)
    link = models.CharField(max_length=60,null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)