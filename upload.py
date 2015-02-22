from app.models import Song,Artist,Album
import os,eyed3
from django.core.files import File

def uploadNow():
	filePath="/home/darth_vader/Desktop/rec/music/uploads/"
	fileList=os.listdir(filePath)

	artist= Artist.objects.get(name="Taylor Swift")

	for music in fileList:
		if music[-4:]==".mp3":
			song= eyed3.load(filePath+music)
			
			title= song.tag.title
			
			album= Album.objects.get(name=song.tag.album)
			genre= song.tag.genre.name
			year= song.tag.recording_date.year
			mp3=File(open(filePath+music,'r'))

			Song(title=title,artist=artist,album=album,genre=genre
				,file=mp3).save()

			print "%s uploaded" % (title)





