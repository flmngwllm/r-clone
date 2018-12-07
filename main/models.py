from django.db import models

# Create your models here.
class Post(models.Model):
    created_at= models.DateTimeField
    title= models.CharField(max_length=200)
    picture= models.CharField(max_length=400, null=True, blank=True)
    content= models.CharField(max_length=400)
    site_url= models.CharField(max_length=400, null=True, blank=True)
    vote_total= models.IntegerField

    def __str__(self):
        return self.name


class Comments(models.Model):
    created_at= models.DateTimeField
    content= models.CharField(max_length=400, null=True, blank=True)
    vote_total=models.IntegerField


    def __str__(self):
        return self.name

