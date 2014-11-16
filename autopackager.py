import sys

sys.path.append('po_deployment')

import nc_deployment, packageutil

if __name__ == '__main__':
    ncdirlist, nccompilelist = nc_deployment.getdeploylist()
    packageutil.generatepackage(ncdirlist, nccompilelist)

    print 'Newegg Central package completed!'
    
    
