import os, time

def getcompiledfiles(dirpath, extension):
    files = os.listdir(dirpath)
    filelist = {}
    for f in files:
        if extension in f:
           filepath = os.path.join(dirpath, f)
           filelist[filepath] = os.path.getsize(filepath), time.ctime(os.path.getmtime(filepath))
    return filelist

def gettemplatefiles(dirpath):
    menutrees = os.walk(dirpath)
    filelist = {}
    for menu in menutrees:
        for f in menu[2]:
            filepath = os.path.join(menu[0], f)
            filelist[filepath] = os.path.getsize(filepath), time.ctime(os.path.getmtime(filepath)), menu[0]
    return filelist

# need merge this function
def getupdatedcfiles(oldfiles, newfiles):
    updatedfiles = [] 
    for key, value in newfiles.items():
        if key in oldfiles:
            oldvalue = oldfiles[key]
            if value[0] != oldvalue[0] or value[1] > oldvalue[1]:
                updatedfiles.append(key)
        else:
            updatedfiles.append(key)
    return updatedfiles

# need merge this function
def getupdatedtfiles(oldfiles, newfiles):
    updatedfiles = {}
    for key, value in newfiles.items():
        if key in oldfiles:
            oldvalue = oldfiles[key]
            if value[0] != oldvalue[0] or value[1] > oldvalue[1]:
                updatedfiles[key] = value[2]
        else:
            updatedfiles[key] = value[2]
    return updatedfiles
            
