#!/usr/bin/env python3
import os


pics_vids = ''
pdfs = ''
words = ''
sheets = ''
extensions = ['.gif', '.jpg', '.jpeg', '.png', '.bmp', '.mp4', '.mov', '.wmv', '.wma', '.pdf',
              '.doc', '.docx', '.txt', '.xlsx']
pic_vid_exts = ['.gif', '.jpg', '.jpeg', '.png', '.bmp', '.mp4', '.mov', '.wmv', '.wma']
pdf_ext = '.pdf'
text_exts = ['.doc', '.docx', '.txt']


def organize_desktop(path):
    global pics_vids
    global words
    global pdfs
    global sheets
    global extensions
    global pic_vid_exts
    global pdf_ext
    global text_exts

    for entry in os.scandir(path=path):
        if os.path.isdir(entry):
            if 'pics_vids' == entry.name:
                pass
            elif 'words' == entry.name:
                pass
            elif 'pdfs' == entry.name:
                pass
            elif 'sheets' == entry.name:
                pass
            else:
                organize_desktop(os.path.join(path, entry))
        else:
            file = str(entry.name)
            src = str(os.path.join(path, entry))
            for ext in extensions:
                if ext in file:
                    dest = ''
                    if ext in pic_vid_exts:
                        print('Found a picture or movie! ' + ext)
                        dest = str(pics_vids) + file
                    elif ext in text_exts:
                        print('Found a word documents ' + ext)
                        dest = str(words) + file
                    elif ext == pdf_ext:
                        print('found a pdf file ' + ext)
                        dest = str(pdfs) + file
                    else:
                        print('Found a spreadsheet ' + ext)
                        dest = str(sheets) + file
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
