import maya.cmds as cmds
import sys # import a module
import os
#reload sys # reload a module
#help(sys) # info about module

if 'C:/Users/Adam/Documents/maya/2017/scripts' not in sys.path:
    sys.path.append('C:/Users/Adam/Documents/maya/2017/scripts') # append a module

#del sys.path[-1] # delete last element in the path array

sourceFile = '/Users/Adam/Documents/maya/2017/scripts/FK_control_module.py'

for p in sys.path:
    print p

def toolWindow():
    winName = 'My Window'
    
    if cmds.window(winName, exists=True):
        cmds.deleteUI(winName)
    
    winName = cmds.window(winName, title='My Window')
    mainCol = cmds.columnLayout(parent=winName, adjustableColumn=True)
    
    cmds.button(label='Create FK control', command='psource(sourceFile)')
    
    myText = cmds.textField()
    theRadius = cmds.textField(myText, q=True, text=True)
    
    cmds.showWindow(winName)

toolWindow()

def psource(module):
    file = os.path.basename(module)
    dir = os.path.dirname(module)

    toks = file.split('.')
    modname = toks[0]

    # Check if dirrectory is really a directory
    if(os.path.exists(dir)):

    # Check if the file directory already exists in the sys.path array
        paths = sys.path
        pathfound = 0
        for path in paths:
            if(dir == path):
                pathfound = 1

    # If the dirrectory is not part of sys.path add it
        if not pathfound:
            sys.path.append(dir)

    exec ('import ' + modname) in globals()    
    exec('reload('+modname+')') in globals() # reload the file to make sure its up to date    
    return modname # return the namespace of the file imported


# Homework:
# NewModule Build a window w/ button to run FK control script (imported as a module)

# Building upon the previous assignment, modify your control script to create a broken FK setup.
# Create a new script (module) that creates a window and interface to import and run the new control script.
# You will submit 2 .py files, the controller script and the window script.
# Remember that in order to import your modules they will need to be saved into a folder specified in the sys.path.
# If you want to specify a working folder, you can append the folder name to the end of the sys.path list.