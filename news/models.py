from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True )
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    prof_image = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length =200)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(first_name__icontains=search_term)
        return profiles

class Project(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'news/')
    description = models.CharField(max_length =60)
    link = models.CharField(max_length =200)
   
    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects    

    def delete_project(self):
        self.delete()

    @classmethod
    def search_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

# class Comments(models.Model):
#     comment = models.CharField(max_length = 300)
#     image = models.ForeignKey(Image, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def save_comment(self):
#         self.save()

#     def delete_comment(self):
#         self.delete()