import sys

sys.path.append('po_deployment')

import nc_deployment, packageutil

SERIALIZE = 's'
GENERATE = 'g'

if __name__ == '__main__':
    ncdirlist = nc_deployment.getdeploylist()
    if len(sys.argv) == 2:
        if sys.argv[1] == SERIALIZE:
            packageutil.serializefiles(ncdirlist)
            print 'Serialize files completed!'
        elif sys.argv[1] == GENERATE:
            packageutil.generatepackage(ncdirlist)
            print 'Newegg Central package completed!'
        else:
            print 'Invalid package command!'
    else:
        print 'Invalid package command!'
    
    
