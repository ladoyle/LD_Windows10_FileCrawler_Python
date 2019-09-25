#!/usr/bin/env python3
import os


pics_vids = ''
pdfs = ''
words = ''
sheets = ''


def organize_desktop(path):
    global pics_vids
    global words
    global pdfs
    global sheets
    os.chdir(path)

    for entry in os.scandir(path=path):
        if os.path.isdir(entry):
            if 'pics_vids' is str(entry.name):
                pass
            elif 'words' is str(entry.name):
                pass
            elif 'pdfs' is str(entry.name):
                pass
            elif 'sheets' is str(entry.name):
                pass
            else:
                organize_desktop(os.path.join(path, entry))
        else:
            src = str(os.path.join(path, entry))
            dest = str(words) + str(entry.name)
            os.rename(src, dest)


if __name__ == '__main__':
    start_path = 'C:/Users/healf/git/LD_Windows10_FileCrawler_Python/tests/'

    try:
        pics_vids = os.path.join(start_path, 'pics_vids/')
        words = os.path.join(start_path, 'words/')
        pdfs = os.path.join(start_path, 'pdfs/')
        sheets = os.path.join(start_path, 'sheets/')

        os.mkdir(pics_vids)
        os.mkdir(words)
        os.mkdir(pdfs)
        os.mkdir(sheets)
    except FileExistsError as exception:
        print(exception)
        print('One of the directories already exists!!')

    organize_desktop(start_path)
else:
    print('This module is not meant to be imported yet...')
