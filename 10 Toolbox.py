# Scripting a Maya Toolbox I
# For this assignment, you will be building some of the tools and components of your Maya toolbox.
# Complete the following list of tools using your knowledge of functions:

# * Freeze Transforms: Freezes the transformations of all selected objects.
# * Delete History: Deletes history for all selected objects.
# * Parent Group: Creates a group for each selection, matching the transformations/pivot of the selection.
# * Parent/Scale Constrain: Parent and scale constrains multiple pairings of selections in a single action.
# * Sequential Renamer: Renames a selection of objects in sequential order using user input in the form "text_##_text".
#     The tool will replace the "#" characters with a sequence, starting at 1, and increasing for each selected object.
#     The number of "#" characters will also determine the length of the replaced sequence number (ex. ## => 01, ### => 001).

# Build a main toolbox window containing user interface elements (buttons, text fields, etc) that will be used to call each of the tools.
# If needed, the main window can call other windows when needed for specific tools.

import maya.cmds as cmds


# --------------------------------------------
# TOOL WINDOW
# PURPOSE: Display buttons for user input.
def toolWindow():
    mainWindow = 'Main Window'
    
    if cmds.window(mainWindow, exists=True):
        cmds.deleteUI(mainWindow)
    
    mainWindow = cmds.window(mainWindow, title='Toolbox')
    mainCol = cmds.columnLayout(parent=mainWindow, adjustableColumn=True)
    
    cmds.button(label='Freeze Tranforms', command='FreezeTransforms()')
    cmds.button(label='Delete History', command='DeleteHistory()')
    cmds.button(label='Parent Group w/ Pivots', command='ParentGroupPivots()')
    cmds.button(label='Parent/Scale Constraints', command='ParentScaleConstraints()')
    cmds.button(label='Sequential Renamer', command='SequentialRenamer(input)')
    input = cmds.textFieldGrp(p=mainCol)
    
    cmds.showWindow(mainWindow)

# --------------------------------------------
# FREEZE TRANSFORMS
# PURPOSE: Freezes the transformations of all selected objects.
def FreezeTransforms():
    # Get selection
    sel = cmds.ls(sl=True)
    
    # If selection exists
    if sel:    
        cmds.makeIdentity(sel, apply=True, t=1, r=1, s=1, n=0)
        
    else:
        cmds.error('ERROR. NO SELECTION. CANNOT FREEZE TRANSFORMATIONS.')


# --------------------------------------------
# DELETE HISTORY
# PURPOSE: Deletes history for all selected objects.
def DeleteHistory():
    # Get selection
    sel = cmds.ls(sl=True)
    
    # If selection exists
    if sel:    
        cmds.delete(sel, constructionHistory=True)
        
    else:
        cmds.error('ERROR. NO SELECTION. CANNOT DELETE HISTORY.')

 
# --------------------------------------------   
# PARENT GROUP W/ PIVOTS
# PURPOSE: Creates a group for each selection, matching the transformations/pivot of the selection.
def ParentGroupPivots():
    # Get selection
    sel = cmds.ls(sl=True)
    
    # The parent group will become the new parent of the selection.
    # That will require that you figure out the current parent of the selection
    # so that you can put the new group in the proper place in the hierarchy.
    
    # If selection exists
    if sel:
        #selParent = cmds.listRelatives('head_geo', parent=True)[0]
        selParent = cmds.listRelatives(sel[0], parent=True)
        newGrp = cmds.parent(newGrp, selParent)
        cmds.parent(sel, newGrp)
        
    else:
        cmds.error('ERROR. NO SELECTION. CANNOT CREATE PARENT GROUP.')


# --------------------------------------------
# PARENT/SCALE CONSTRAINTS
# PURPOSE: Parent and scale constrains multiple pairings of selections in a single action.
def ParentScaleConstraints(alternate=False):
    print ('ParentScaleConstraints')
    sels = cmds.ls(sl=True) # create a list of selected items
    
    print sels # print a list of selected items
    print(len(sels)) # print number of selected items
    
    # check if there is an odd or even number of items selected
    if not (len(sels) % 2):        
        constrainerList, constraineeList = [],[] # create two lists
        
        print 'even'
        # get length of list
        length = len(sels)/2
        halfLength = length/2
        
        if not alternate:                
            # devide in half (slice)
            # sels[Start:End:Step]
            print sels[:length]
                
            # create 2 lists: controls & joints  
            constrainerList = sels[:halfLength]
            constraineeList = sels[halfLength:]
                  
            # loop using same index
            for i in range(halfLength):
               print 'constrain %s to %s' % (constrainerList[i], constraineeList[i])
        
        else:
            constrainerList = sels[::2]
            constraineeList = sels[1::2]
            
       # create constraints
    else:
        print 'odd'
        cmds.error('ERROR. UNEVEN NUMBER OF SELECTIONS. PLEASE SELECT AN EQUAL NUMBER OF CONTROLS AND JOINTS.')


# --------------------------------------------
# SEQUENTIAL RENAMER
# PURPOSE: Renames a selection of objects in sequential order using user input in the form "text_##_text".
#          The tool will replace the "#" characters with a sequence, starting at 1, and increasing for each selected object.
#          The number of "#" characters will also determine the length of the replaced sequence number (ex. ## => 01, ### => 001).
def SequentialRenamer(input):
    # Get selection
    sel = cmds.ls(sl=True)
    
    # If selection exists
    if sel:
        for i in sel:
            cmds.rename(i, 'geo')
        
        cmds.rename(sel, 'head_geo')

        
    # Get selection (hierarchy?)
    # Rename selection (optional)
    # Input "...#" (special character to denote replacement)
        # -> TextBox/Win
    # Get text (func())
    # Loop through selection
        # -> Convert # to numberstrings use range index (str.replace(), str.zfill())
        # -> Rename the obj to converted name   

        
    else:
        cmds.error('ERROR. NO SELECTION. CANNOT RENAME OBJECTS.')

    # lambda functions?
    
# ____________________________________________
toolWindow()