import os
import sys
    

def cleanup (path):
    flag = False
    try:
        os.chdir(path)
        flag = True
    except:
        flag = False
        
    try:
        for root, dirs, files in os.walk(path):
            for file in files:
                try:
                    os.remove(file)
                except:
                    pass
            for sub in dirs:
                try:
                    os.rmdir(sub)
                except:
                    pass
        
    except:
        pass        
    return flag 