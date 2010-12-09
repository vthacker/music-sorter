
#!/usr/bin/python
import os
import fnmatch
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import shutil
def gen_find(filext,top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filext):
            yield os.path.join(path,name)

songdir=gen_find("*.mp3","/home/varun/Desktop/varun/")
#song_dir will contain all songs to be sorted.Pass the directory to be searched for songs as second paramater to this function.
 
songdest="/home/varun/Desktop/Destination/"  #where you want to finally place your songs.
for song in songdir:
	audio = MP3(song,ID3=EasyID3)
	a=audio.values
	print callable(a)
	b=a() 			
	l=len(b)
	if l==1:
		folder_artist=b[0]
		folder_album="Unknown Album"
	if l==0:
		folder_artist="Unknown Artist"
		folder_album="Unknown Album"
	else:		
		folder_artist=b[l-1]
		folder_album=b[0]
	check=os.path.join(songdest,folder_artist[0]+'/')
	try:
		os.mkdir(check)
	except  OSError:
		pass
	check2=os.path.join(check,folder_album[0]+'/')
	try:
		os.mkdir(check2)
	except OSError:
		pass
	shutil.move(song,check2)
print "success"
