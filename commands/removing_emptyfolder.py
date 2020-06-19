#!/usr/bin/env python3
import os

def r_e_f(path) :
    ct = 0 
    for file in os.listdir(path) :
        if file == 'No' :
            continue 
        if os.path.isdir(file) :
            if not os.listdir(file) :
                print('Removing ' + os.path.join(os.getcwd(),file)) 
                os.removedirs(os.path.join(os.getcwd() , file))
                ct += 1
            else :
                print(file + ' is not empty')
        else :
            print(file + ' is not a dir')
    return ct

def removing_empty_folder() :
    cnt = r_e_f(os.getcwd())
    print('Total ' + str(cnt) + ' folder is deleted.')

if __name__ == "__main__":
    removing_empty_folder()

    