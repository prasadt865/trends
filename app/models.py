from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField,EmbeddedModelField
# Create your models here.

class Artist(models.Model):
	name= models.CharField(max_length=20)
	bio= models.TextField()
	artist_pic= models.FileField(upload_to="artist/")

	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ["name"]

class Album(models.Model):
	name= models.CharField(max_length=20)
	year= models.DateTimeField()
	album_art= models.FileField(upload_to="album/")

class Song(models.Model):
	title= models.CharField(max_length=20)
	artist=ListField(EmbeddedModelField(Artist))
	genre= ListField()
	file= models.FileField(upload_to="songs/")

class UserLog(models.Model):
	song= models.ManyToManyField(Song)
	user= models.ManyToManyField(User)
	time= models.DateTimeField(auto_now_add=True)



