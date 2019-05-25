import os

print('\n' + os.getcwd())

os.chdir('C:/Users/healf/git/LD_Windows10_FileCrawler_Python/tests')
print(os.stat('text.txt'))

for dirpath, filenames in os.walk('C:/Users/healf/git/'):
    print('Current Path:= ', dirpath)
    print('File:= ', filenames)
    print()