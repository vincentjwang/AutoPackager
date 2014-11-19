import sys

sys.path.append('po_deployment')

import nc_deployment, api_deployment, job_deployment, packageutil

SERIALIZE = '-s'
GENERATE = '-g'

NC_DEPLOYMENT = '-n'
JOB_DEPLOYMENT = '-j'
API_DEPLOYMENT = '-a'

def getdeploylist(deploytype):
    if deploytype == NC_DEPLOYMENT:
        return nc_deployment.getdeploylist()
    elif deploytype == JOB_DEPLOYMENT:
        return job_deployment.getdeploylist()
    elif deploytype == API_DEPLOYMENT:
        return api_deployment.getdeploylist()
    else:
        raise Exception('Deploy type error!')

if __name__ == '__main__':
    if len(sys.argv) == 3:
        dirlist = getdeploylist(sys.argv[2])
        if sys.argv[1] == SERIALIZE:
            packageutil.serializefiles(dirlist)
            print 'Serialize files completed!'
        elif sys.argv[1] == GENERATE:
            packageutil.generatepackage(dirlist)
            print 'Package completed!'
        else:
            print 'Invalid package command!'
    else:
        print 'Invalid package command!'
    
    
