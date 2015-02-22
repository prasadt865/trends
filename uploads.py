import eyed3
from django.core.files import File
from app.models import Song
path="/home/darth_vader/Desktop/rec/music/uploads/"
def upload(fileName):
	song=eyed3.load(path+fileName)

	title= song.tag.title
	album= song.tag.album
	genre= song.tag.genre.name
	year= song.tag.recording_date.year
	artist= song.tag.artist
	mp3= File(open(path+fileName))

	Song(title=title,artist=artist,genre=genre,year=year,album=album,file=mp3).save()





