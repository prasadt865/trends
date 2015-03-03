import eyed3
from django.core.files import File
from app.models import Song
import os


def upload():
	path="/home/darth_vader/Desktop/rec/music/uploads/"
	file_list=os.listdir(path)

	for f in file_list:
		song=eyed3.load(path+f)

		title= song.tag.title
		album= song.tag.album
		genre= song.tag.genre.name
		year= song.tag.recording_date.year
		artist= song.tag.artist
		mp3= File(open(path+f),'r')

		Song(title=title,artist=artist,genre=genre,year=year,album=album,file=mp3).save()







'''
def upload(fileName):
	song=eyed3.load(path+fileName)

	title= song.tag.title
	album= song.tag.album
	genre= song.tag.genre.name
	year= song.tag.recording_date.year
	artist= song.tag.artist
	mp3= File(open(path+fileName))

	Song(title=title,artist=artist,genre=genre,year=year,album=album,file=mp3).save()


'''


