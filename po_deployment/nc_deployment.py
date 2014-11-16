def getdeploylist():
    dirlist = []
    dirlist.append((r'D:\VSTS\01_PO\03_Code\01_SourceCode\Silverlight PO Restful\NeweggCentral\ClientBin',
                    r'C:\Users\Administrator\Desktop\Silverlight PO Restful\NeweggCentral\Client\ClientBin',
                    '.txt'))
    # dirlist.append(('source bin', 'target bin', '.dll'))
    # dirlist.append(('source configer', 'target configer', '.config'))
    dirlist.append((r'D:\VSTS\01_PO\03_Code\01_SourceCode\Silverlight PO Restful\NeweggCentral.ServiceCenter\Template',
                    r'C:\Users\Administrator\Desktop\Silverlight PO Restful\NeweggCentral\Service\Template'))
    
    compilelist = []
    compilelist.append('Client')
    compilelist.append('Service')

    return dirlist, compilelist
