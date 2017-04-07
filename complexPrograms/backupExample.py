#! python2

import os, zipfile, shutil

def backup(folder):
    folder = os.path.abspath(folder)

    if not os.path.isdir('./TestBackup'):
        os.makedirs('./TestBackup')

    number = 1
    while True:
        archiveFilename = os.path.basename(folder) + '-' + str(number) + '.zip'
        if not os.path.isfile('./TestBackup/Test-' + str(number) + '.zip'):
            break
        number += 1
    print(str(archiveFilename))

    print('Preparing %s...' % (archiveFilename))
    backupArchive = zipfile.ZipFile(archiveFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupArchive.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '-'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            elif filename.endswith('.py'):
                backupArchive.write(os.path.join(foldername, filename))
    backupArchive.close()
    shutil.move(('./%s' % str(archiveFilename)), './TestBackup')
    print('Completed.')


backup('./Test')
