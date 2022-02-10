import maya.cmds as cmds

def CreateLoc():
	sels = cmds.ls(sl=True)
	
	dups = cmds.duplicate(sels, rr=True)
	dups = cmds.polyUnite(dups, ch=True, mergeUVSets=True, centerPivot=True)
	bbox = cmds.xform(dups[0], boundingBox=True)
	pivot = [ (bbox[0] + bbox[3])/2, (bbox[1] + bbox[4])/2, (bbox[2] + bbox[5])/2 ]
	
	#xPivot = (bbox[0] + bbox[3])/2
	#yPivot = (bbox[1] + bbox[4])/2
	#zPivot = (bbox[2] + bbox[5])/2

	
	cmds.delete(dups, ch=True)
	cmds.delete(dups)
	
	loc = cmds.spaceLocator()[0]
	cmds.xform(loc, translation=pivot, worldSpace=True)




def CreateLoc2(option):
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
		
		
		
		
CreateLoc()