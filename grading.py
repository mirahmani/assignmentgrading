'''Written by Miranti Rahmani
29 September 2017'''

from os import listdir,chdir, mkdir, remove
from os.path import join, exists, isfile, splitext, basename
import zipfile, shutil

dirbase = '/Volumes/DATA/_Assistance' #directory to put assignment folder
assignment = 'Assignment' + input('assignment: ') #input assignment number. e.g. 1a, 1b, 2, etc.
dirpath = dirbase + '/' + assignment
chdir(dirbase)

#Create submission folder if not existed yet
if not exists(dirpath):
    mkdir(dirpath)
    chdir(dirpath)
    mkdir('solution')
    mkdir('done')
else: #assignment folder and submission.zip already exists
    subdir = dirpath + '/submissions'
    chdir(subdir)
    allcontent = listdir(subdir)
    onlyfiles = [files for files in allcontent if (isfile(join(subdir, files)) and not files.startswith('.'))]
    #for i in onlyfiles:
    #    print(i)
    currentgroupname = ''
    prevgroupname = ''
    for i in onlyfiles:
        prevgroupname = currentgroupname
        if i.endswith('.zip'):
            zipp = join(subdir,i)
            zipname = splitext(basename(i))[0]
            zipfolder = join(subdir,zipname)
            mkdir(zipfolder)
            zip_ref = zipfile.ZipFile(zipp, 'r')
            zip_ref.extractall(zipfolder)
            zip_ref.close()
            remove(zipp)
            currentgroupname = i.split('_')[0] #take only the first section of file name (assignmentgroupXX)
        else: #not a zip file
            currentgroupname = i.split('_')[0]
            if (currentgroupname != prevgroupname): #file belongs to different group
                #create new group folder
                grppath = join(subdir,currentgroupname)
                mkdir(grppath)
                #move file to new group folder
                source = join(subdir, i)
                destination = join(grppath,i)
                shutil.move(source,destination)
            else: #still belongs to same group name
                #move file to folder
                source = join(subdir, i)
                destination = join(grppath, i)
                shutil.move(source, destination)