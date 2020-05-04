import glob
import runpy

wildcard = ".\\**\\*.py"
modules = glob.glob(wildcard, recursive=True)

numModules = len(modules)

''' This is the index of the file - change this to start later in the list '''
n = 20

for moduleFileName in modules[n:]:

    n = n + 1

    print("==================================================================")
    print("TEST CASE ANALYSIS OF MODULE: ", moduleFileName)
    print("Module %d out of %d: " % (n, numModules))

    runpy.run_path(moduleFileName, run_name='__main__')
