#! python2

import os, zipfile, shutil

def backup(folder):
    folder = os.path.abspath(folder)

    if not os.path.isdir('/archive path/TestBackup'):
        os.makedirs('/archive path/TestBackup')

    number = 1
    while True:
        archiveFilename = os.path.basename(folder) + '-' + str(number) + '.zip'
        print(str(archiveFilename))
        if not os.path.exists(archiveFilename):
            break
        number += 1

    print('Preparing %s...' % (archiveFilename))
    backupArchive = zipfile.ZipFile(archiveFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupArchive.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '-'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupArchive.write(os.path.join(foldername, filename))
    backupArchive.close()
    shutil.move(('/working path/%s' % str(archiveFilename)), '/dest path/TestBackup')
    print('Completed.')


backup('/source dir/Test')
