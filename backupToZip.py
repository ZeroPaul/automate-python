#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile, os

def backupToZip(folder):
    """TODO: Docstring for backupToZip.
    : Backup the entire contens of FOLDER into ZIP file.
    """
    folder = os.path.abspath(folder)     #make sure folders is absolute

    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number = number + 1
    print('Creating %s...' % (zipFileName))
    backupZip = zipfile.ZipFile(zipFileName, 'w')
    
        

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
        # for filename in filenames:
        #     newBase / os.path.base(folder) + '_'
        #     if filename.startwith(newBase) and filename.endwith('.zip'):
        #         continue
        #     backupZip.write(os.path.join(foldername, filename))
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')

backupToZip('../demo')
        
