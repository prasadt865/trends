from django.db import models
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField,EmbeddedModelField
# Create your models here.
'''
class Artist(models.Model):
	name= models.CharField(max_length=20)
	bio= models.TextField()
	artist_pic= models.FileField(upload_to="artist/",blank=True)

	def __unicode__(self):
		return self.name
	
	class Meta:
		ordering = ["name"]

class Album(models.Model):
	name= models.CharField(max_length=20)
	year= models.PositiveSmallIntegerField(blank=True, null=True)
	album_art= models.FileField(upload_to="album/",blank=True)

	def __unicode__(self):
		return "%s %s" %(self.name,self.year)
'''

class Song(models.Model):
	title= models.CharField(max_length=50)
	artist=models.CharField(max_length=50)
	album= models.CharField(max_length=50)
	year=models.PositiveSmallIntegerField(blank=True, null=True)
	genre= models.CharField(max_length=50)
	file= models.FileField(upload_to="songs/")

	def __unicode__(self):
		return "%s-%s-%s" % (self.title,self.album,self.artist)

	class Meta:
		ordering = ["title"]

class Playlist(models.Model):
	user= models.ForeignKey(User)
	name= models.CharField(max_length=50)
	songs= ListField(EmbeddedModelField('Song'))
	date= models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "%s %s %s" % (self.name,self.user,self.date)

	class Meta:
		ordering = ["name"]

class UserLog(models.Model):
	song= models.ForeignKey(Song)
	user= models.ForeignKey(User)
	time= models.DateTimeField(auto_now_add=True)



