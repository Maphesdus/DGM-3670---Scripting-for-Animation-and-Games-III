# Scripting a Maya Toolbox
# For this assignment, you will be building some of the tools and components of your Maya toolbox.
# Complete the following list of tools using your knowledge of functions:


# * Random Placement Generator (Tree Spawner.mel)
# * Sequential Renamer Tool
# * Center Locator Tool
# * Control Creator
# * FK Joint Hierarchy Builder
# * Your individual tool



# Build a main toolbox window containing user interface elements (buttons, text fields, etc) that will be used to call each of the tools.
# If needed, the main window can call other windows when needed for specific tools.

import maya.cmds as cmds
import maya.mel as mel

# --------------------------------------------
# TOOL WINDOW
# PURPOSE: Display buttons for user input.
def toolWindow():
    mainWindow = 'Main Window'
    
    if cmds.window(mainWindow, exists=True):
        cmds.deleteUI(mainWindow)

    mainWindow = cmds.window(mainWindow, title='Toolbox')
    mainCol = cmds.columnLayout(parent=mainWindow, adjustableColumn=True)    
    
    cmds.text('Main Toolbox:\n')
    
    
    # Create 1st row for Random Tree Placement:
    treeRowLayout = cmds.rowLayout(parent=mainCol, numberOfColumns=6)    
    cmds.text(parent=treeRowLayout, label="Random Tree Placer: ");
    xRange = cmds.intField(parent=treeRowLayout, value=15)
    yRange = cmds.intField(parent=treeRowLayout, value=25)
    zRange = cmds.intField(parent=treeRowLayout, value=30)
    cmds.button(parent=treeRowLayout, label='Place Trees', command='RndPlace("xRange", "yRange", "zRange")')

    # Create 2nd row for Sequential Renamer:
    renamerRowLayout = cmds.rowLayout(parent=mainCol, numberOfColumns=3)  
    cmds.text(parent=renamerRowLayout, label="Sequential Renamer : ");
    input = cmds.textFieldGrp(parent=renamerRowLayout, text='')
    cmds.button(parent=renamerRowLayout, label='Rename Selected Objects', command='SequentialRenamer(input)')
    
    # Create 3rd row for other tools:
    toolColumnLayout = cmds.columnLayout(parent=mainCol) 
    #toolRowLayout = cmds.rowLayout(parent=mainCol, numberOfColumns=6)  
    cmds.button(parent=toolColumnLayout, label='Center Locator', command='CreateLoc()')
    cmds.button(parent=toolColumnLayout, label='Control Creator', command='')
    cmds.button(parent=toolColumnLayout, label='FK Joint Hierarchy Creator', command='')
    
    # Create 4th row for other tools:
    toolColumnLayout = cmds.columnLayout(parent=mainCol) 
    cmds.text(parent=toolColumnLayout, label='\nAdditional Tools:')
    cmds.button(parent=toolColumnLayout, label='Freeze Tranforms', command='FreezeTransforms()')
    cmds.button(parent=toolColumnLayout, label='Delete History', command='DeleteHistory()')
    cmds.button(parent=toolColumnLayout, label='Parent Group w/ Pivots', command='ParentGroupPivots()')
    cmds.button(parent=toolColumnLayout, label='Parent/Scale Constraints', command='ParentScaleConstraints()')
    cmds.button(parent=toolColumnLayout, label='Build Joint Chain from Selected CV Curve', command='BuildJointChainFromSelection()')
    cmds.button(parent=toolColumnLayout, label='Show/Hide Local Rotation Axes', command='ShowHideLocalRotationAxes()')
    cmds.button(parent=toolColumnLayout, label='Switch Unlocked Influences', command='SwitchUnlockedInfluences()')
    
    cmds.showWindow(mainWindow)
	

# --------------------------------------------
# RANDOM PLACEMENT GENERATOR (Tree Spawner.mel)
# PURPOSE: Generates and randomly places trees.

def RndPlace(x, y, z):
    #import "Tree Spawner.mel"
    #mel.eval('source "Tree Spawner.mel"')
    mel.eval('source "C:/Users/10435286/Documents/maya/scripts/Tree Spawner.mel"')
    mel.eval('DuplicateTrees("x", "y", "z")')







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
            cmds.rename(i, "" + input)
        
        cmds.rename(sel, 'head_' + input)

        
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





# --------------------------------------------
# CREATE LOCATOR
# PURPOSE:	Create a series of locators at the center of each selected object,
#			or create one locator in center of the scene if no objects are selected.
def CreateLoc(option):
	sels = cmds.ls(sl=True)
	
	if option is 1:
		dups = cmds.duplicate(sels, rr=True)
		dups = cmds.polyUnite(dups, ch=True, mergeUVSets=True, centerPivot=True)
		bbox = cmds.xform(dups[0], boundingBox=True)
		pivot = [ (bbox[0] + bbox[3])/2, (bbox[1] + bbox[4])/2, (bbox[2] + bbox[5])/2 ]
		
		cmds.delete(dups, ch=True)
		cmds.delete(dups)
		
		loc = cmds.spaceLocator()[0]
		cmds.xform(loc, translation=pivot, worldSpace=True)
	
	elif options is 2:
		for sel in sels:
			pivot = cmds.xform(sel, q=True, rp=True)
			print pivot
			loc = cmds.spaceLocator()[0]
			cmds.xform(loc, translation=pivot, worldSpace=True)
		
		
		
	

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
# Build Joint Chain from Selection
#    Based on the order of objects selected, this will create a joint at the position of each object in one continuous chain.
def BuildJointChainFromSelection():
    # array of selected objects
    sel = cmds.ls( selection=True )
    
    # name of the curve to convert
    lastSelect = int(len(sel)) -1
    curveSel = sel[lastSelect]
    
    # print lastSelect
    #print curveSel
    
    #find the number of CVs (Degree + Spans)
    numCVs = int(cmds.getAttr (curveSel+'.degree'))+ (cmds.getAttr (curveSel+'.spans'))
    #print numCVs
    
    # selection must be clear
    cmds.select(clear=True)
    
    #For each CV in the Curve create a joint.
    
    i=0
    while 1:
        if not ( i < numCVs ):
            break
        cvPosition = (cmds.getAttr (curveSel+'.cv['+(str(i))+']'))
        if (i == 0):
        	cmds.joint(n=curveSel+'_jointRoot',p = cvPosition[0])
        if (i == (numCVs-1)):
        	cmds.joint(n=curveSel+'_jointEnd', p = cvPosition[0])
        if(i>0)and(i != numCVs-1):
        	cmds.joint(n=curveSel+'_joint_'+(str(i)),p = cvPosition[0])	
        i+=1
     
    # reorient the joints    
    i=1
    while 1:
    	if not (i < numCVs-1):
    		break
    	#find the name of the current Joint
    	currentJoint = (curveSel+'_joint_'+(str(i)))
    	cmds.joint(currentJoint,e=True,zso=True,oj="xyz")
    	i+=1
        

# --------------------------------------------
# Show/Hide Local Rotation Axes (Toggle)
#    To help in joint orientation, this tool will take the current joint selection and set the displayLocalAxis to on and
#    unhide the following list of attributes in the channel box:
#        displayLocalAxis, jointOrientX, jointOrientY, jointOrientZ
#    If this previous step has already been run, this script will toggle the displayLocalAxis to off and hide the list of attributes from the channelbox.
def ShowHideLocalRotationAxes():
    # Get selection
    sel = cmds.ls(sl=True)
    
    # If selection exists
    if sel:
        print(sel)
        switchAxesDisplay=False
        #displayLocalAxis = on
        #jointOrientX = show
        #jointOrientY = show
        #jointOrientZ = show
        
        if not (switchAxesDisplay):
            cmds.setAttr("%s.displayLocalAxis" % sel, channelBox=True)        
            cmds.setAttr("%s.jointOrientX " % sel, channelBox=True)
            cmds.setAttr("%s.jointOrientY " % sel, channelBox=True)
            cmds.setAttr("%s.jointOrientZ " % sel, channelBox=True)
            switchAxesDisplay=True
        else: 
            cmds.setAttr("%s.displayLocalAxis" % sel, channelBox=False)        
            cmds.setAttr("%s.jointOrientX " % sel, channelBox=False)
            cmds.setAttr("%s.jointOrientY " % sel, channelBox=False)
            cmds.setAttr("%s.jointOrientZ " % sel, channelBox=False)
            switchAxesDisplay=False
        
    else:
        cmds.error('ERROR. NO SELECTION. CANNOT TOGGLE LOCAL ROTATION AXES.')
    


# --------------------------------------------
# Switch Unlocked Influences
#    When using the Paint Weights tool, this tool will step through and select the unlocked joints in the skin cluster one at a time.
#    This will allow the artist to jump quickly between influences without the need to search through the entire list of influences.
#    One approach to the script would be to find the name of the current skin cluster, query a list of all of the influences, query  those that are unlocked.
#    Once you have that list, you can compare that with your currently selected influence and change the selection to another influence.
def SwitchUnlockedInfluences():
    # Get selection
    sel = cmds.ls(sl=True)
    
    # If selection exists
    if sel:
        print(sel)
        # 1. find the name of the current skin cluster
        # 2. query a list of all of the influences
        # 3. query  those that are unlocked
        # 4. compare that with your currently selected influence
        # 5. change the selection to another influence
        
    else:
        cmds.error('ERROR. NO SELECTION. CANNOT SWITCH UNLOCKED INFLUENCES.')
    
# ____________________________________________
toolWindow()


# Scripting a Maya Toolbox II
#    Build upon the previous assignment by creating the following new tools and incorporating them into your toolbox:

# Build Joint Chain from Selection
#    Based on the order of objects selected, this will create a joint at the position of each object in one continuous chain.

# Toggle Local Rotation Axes
#    To help in joint orientation, this tool will take the current joint selection and set the displayLocalAxis to on and
#    unhide the following list of attributes in the channel box:
#        displayLocalAxis, jointOrientX, jointOrientY, jointOrientZ
#    If this previous step has already been run, this script will toggle the displayLocalAxis to off and hide the list of attributes from the channelbox.

# Switch Unlocked Influences
#    When using the Paint Weights tool, this tool will step through and select the unlocked joints in the skin cluster one at a time.
#    This will allow the artist to jump quickly between influences without the need to search through the entire list of influences.
#    One approach to the script would be to find the name of the current skin cluster, query a list of all of the influences, query  those that are unlocked.
#    Once you have that list, you can compare that with your currently selected influence and change the selection to another influence.



