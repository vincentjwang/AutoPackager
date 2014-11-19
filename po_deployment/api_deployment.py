def getdeploylist():
    dirlist = []
    dirlist.append(('source bin', 'target bin', '.dll'))
    dirlist.append(('source configer', 'target configer', '.config'))
    dirlist.append(('source template', 'target template'))
    return dirlist
