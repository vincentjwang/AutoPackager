import os, shutil, filegenerator, pickle

DEPLOY_PICKLE = 'deploydata.pickle'

def getfiles(dirlist):
    filelist = []
    for d in dirlist:
        if len(d) == 3:
            filelist.append((filegenerator.getcompiledfiles(d[0], d[2]), d[1]))
        else:
            filelist.append((filegenerator.gettemplatefiles(d[0]), d[1]))
    return filelist

def serializefiles(dirlist):
    deployfiles = getfiles(dirlist)
    with open(DEPLOY_PICKLE, 'wb') as f:
        pickle.dump(deployfiles, f, pickle.HIGHEST_PROTOCOL)

def generatepackage(dirlist):
    oldfilelist = []
    with open(DEPLOY_PICKLE, 'rb') as f:
        oldfilelist = pickle.load(f)
    mockupfileupdate()
    newfilelist = getfiles(dirlist)
    for i in range(0, len(dirlist)):
        if len(dirlist[i]) == 3:
            updatedfiles = filegenerator.getupdatedcfiles(oldfilelist[i][0], newfilelist[i][0])
            if updatedfiles:
                if not os.path.exists(dirlist[i][1]):
                    os.makedirs(dirlist[i][1])
                for f in updatedfiles:
                    shutil.copy(f, dirlist[i][1])
        else:
            updatedfiles = filegenerator.getupdatedtfiles(oldfilelist[i][0], newfilelist[i][0])
            if updatedfiles:
                for key, value in updatedfiles.items():
                    targetpath = dirlist[i][1] + value.replace(dirlist[i][0], '')
                    if not os.path.exists(targetpath):
                        os.makedirs(targetpath)
                    shutil.copy(key, targetpath)
            

def mockupfileupdate():
    f = open(r'D:\VSTS\01_PO\03_Code\01_SourceCode\Silverlight PO Restful\NeweggCentral\ClientBin\NeweggCental.xap.txt', 'w')
    f.write('456')
    f.close()
    f = open(r'D:\VSTS\01_PO\03_Code\01_SourceCode\Silverlight PO Restful\NeweggCentral\ClientBin\1.txt', 'w')
    f.close()

    f = open(r'D:\VSTS\01_PO\03_Code\01_SourceCode\Silverlight PO Restful\NeweggCentral.ServiceCenter\Template\EmailTemplate\e1.txt', 'w')
    f.write('email template')
    f.close()

    f = open(r'D:\VSTS\01_PO\03_Code\01_SourceCode\Silverlight PO Restful\NeweggCentral.ServiceCenter\Template\SSBTemplate\e2.txt', 'w')
    f.write('ssb template')
    f.close()

    f = open(r'D:\VSTS\01_PO\03_Code\01_SourceCode\Silverlight PO Restful\NeweggCentral.ServiceCenter\Template\SSBTemplate\VendorSSB\v1.txt', 'w')
    f.write('vendor ssb template')
    f.close()
