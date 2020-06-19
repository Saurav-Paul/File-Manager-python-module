#!/usr/bin/env python3
import os

def find_files() :
    # finding the files extension
    extension_set = set() 

    for file in os.listdir(os.getcwd()) :
        try :
            extension = file.rsplit(sep = '.',maxsplit= 1)
            extension_set.add(extension[1].lower())
        except IndexError :
            continue
    return extension_set

			

def create_dir(extension_set,video_formats,audio_formats,image_formats,Fname):
    for dir in extension_set:
        try:
            if dir in video_formats:
                os.makedirs(Fname[0])
            elif dir in audio_formats:
                os.makedirs(Fname[1])
            elif dir in image_formats:
                os.makedirs(Fname[2])
            else:
                os.makedirs(dir+'_files')
        except FileExistsError:
            continue

			
def arrange_files(ex,video_formats,audio_formats,image_formats,Fname) :
    print(video_formats)
    for file in os.listdir(os.getcwd()) :
        try :
            ex = file.rsplit(sep = '.', maxsplit=1)
            ext = ex[1].lower()
            if ext in video_formats:
                os.rename(file,Fname[0]+'/'+file)
                print(file)
            elif ext in audio_formats:
                os.rename(file,Fname[1]+'/'+file)
            elif ext in image_formats:
                os.rename(file,Fname[2]+'/'+file)
            else :
                os.rename(file,ext + '_files/'+file)
        except :
            print('not granted = ' + file)
            continue
		

def file_organizer() :
    video_formats = {'mkv','mp4','webm','avi','flv','wmv'}
    audio_formats = {'mp3','m4a','flac','wav','wma','aac'}
    image_formats = {'jpeg','png','gif','tiff','tif','bmp','jpg','raw'}
    Fname = ['videos','audios','pictures']
    ex = find_files()
    ex.remove('py')
    print(ex)
    print(video_formats)
    print(audio_formats)
    print(image_formats)
    create_dir(ex,video_formats,audio_formats,image_formats,Fname)
    arrange_files(ex,video_formats,audio_formats,image_formats,Fname)
    print('\n---FIles Arranged---\nScripted By Saurav Paul.\n')

if __name__ == "__main__":
    file_organizer()
    
