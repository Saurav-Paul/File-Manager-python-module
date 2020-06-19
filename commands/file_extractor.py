#!/usr/bin/env python3
import os

def file_out(path,dest) :
    for file in os.listdir(path):
        try :
            if os.path.isdir(file):
                file_out(os.path.join(path,file),dest)
            else:
                c_file = os.path.join(path,file)
                os.rename(c_file,dest+'/'+file)
        except :
            print('Unknown error occured. :(')


if __name__ == "__main__":
    sure = input('If you want extract all the files then print write yes : ')
    if sure.lower() == 'yes' :
        now = os.getcwd()
        file_out(now,now)
        print('\n---FIles Extracted---\nScripted By Saurav Paul.\n')
    
