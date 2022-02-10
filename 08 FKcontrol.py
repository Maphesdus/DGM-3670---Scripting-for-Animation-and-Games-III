import maya.cmds as cmds

# Homework:
# * Add a for-loop to create a control for each selection if there are multiple selections
# * Create separate functions for changeColor and position/orientation.
# * Revise the changeColor fuction to set the overrideColor value within the changeColor function.


# Create a separate function to color the controls, requiring the control name and a color as parameters.
# The function should be called from within the control creation script.



#----------------------------------
def changeColor(colorIndex):
        if colorIndex == 'blue':
            colorVal = 6
        elif colorIndex == 'red':
            colorVal = 13
        elif colorIndex == 'yellow':
            colorVal = 17
        elif colorIndex == 'green':
            colorVal = 14
        elif colorIndex == 'purple':
            colorVal = 9
        else:
            colorVal = 5
        # Find shape node  
        # Use setAttr to enable override
        #cmds.setAttr('%s.overrideEnabled' % ctrlGrp, 1)
        
        # Use setAttr to assign color
        #cmds.setAttr('%s.overrideColor' % ctrlGrp, colorVal)
        
        #ctrlShape
        #setAttr(ctrlShape, override, colorVal)
        
        return colorVal


# Create a separate function that matches the position and rotation of one node to another,
# requiring two nodes as parameters. In this case, the control group and the selection will
# be used as arguments. The function should be called from within the control creation script.


#----------------------------------
def repoReor(jnt, ctrlGrp):
        # > parent - zero out
        ctrlGrp = cmds.parent(ctrlGrp, jnt)[0]
    
        #reposition/reorient
        cmds.setAttr('%s.translateX' % ctrlGrp, 0)
        cmds.setAttr('%s.translateY' % ctrlGrp, 0)
        cmds.setAttr('%s.translateZ' % ctrlGrp, 0)
        
        cmds.setAttr('%s.rotateX' % ctrlGrp, 0)
        cmds.setAttr('%s.rotateY' % ctrlGrp, 0)
        cmds.setAttr('%s.rotateZ' % ctrlGrp, 0)
        
        cmds.setAttr('%s.scaleX' % ctrlGrp, 1)
        cmds.setAttr('%s.scaleY' % ctrlGrp, 1)
        cmds.setAttr('%s.scaleZ' % ctrlGrp, 1)
        
        # > unparent
        cmds.parent(ctrlGrp, world=True)


#----------------------------------
#create control
def createControl(color):
     sel = cmds.ls(sl=True)
     if sel:
         selList = cmds.select (sel, hi=True)
         selList = cmds.ls(sl=True)
         
         for jnt in selList:
             currentJoint = jnt
             cmds.select(currentJoint, replace=True)
             jointObject = cmds.ls(sl=True)
             rel = cmds.listRelatives(children=True)
             print(rel)
             
             if(rel):
                 createCircle = circle(color)
                 
                 if (len(rel) > 1):                     
                     cmds.error("ERROR. JOINT HAS MULTIPLE CHILDREN.")
                     break
             
                 #else:
                     #createCircle = circle(color)
             
     else:
         createCircle = circle(color)


#----------------------------------
#create CIRCLE control
def circle(colorIndex):
    # if selection exists, create control : position/orient to selection
    # else create control at origin
    
    sel = cmds.ls(sl=True)
    colorVal = changeColor(colorIndex); # change color

    # check for multiple selections
    if sel:        
        for jnt in sel:
            print jnt
                        
            #rename control
            name = '%s_ctrl' % jnt
            
            # Create Circle:
            ctrl = cmds.circle(name=name, c=[0,0,0], nr=[0,1,0], sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=1)[0]
            
            #create group (parent -> control)
            ctrlShape = cmds.listRelatives(ctrl, shapes=True, children=True)[0]
            ctrlGrp = cmds.group(empty=True, name='%s_Grp' % ctrl)
            ctrl = cmds.parent(ctrl, ctrlGrp, a=True)[0]        
            
            #reposition/reorient
            repoReor(jnt, ctrlGrp)
            
            # Find shape node  
            # Use setAttr to enable override
            cmds.setAttr('%s.overrideEnabled' % ctrlGrp, 1)
            
            # Use setAttr to assign color
            cmds.setAttr('%s.overrideColor' % ctrlGrp, colorVal)
            
        return ctrl           
        
    else:      
        ctrl = cmds.circle(c=[0,0,0], nr=[0,1,0], sw=360, r=1, d=3, ut=0, tol=0.01, s=8, ch=1)[0]
        
        #create group (parent -> control)
        ctrlShape = cmds.listRelatives(ctrl, shapes=True, children=True)[0]
        ctrlGrp = cmds.group(empty=True, name='%s_Grp' % ctrl)
        ctrl = cmds.parent(ctrl, ctrlGrp, a=True)[0]

        
        changeColor(colorIndex);
        
        # Find shape node  
        # Use setAttr to enable override
        cmds.setAttr('%s.overrideEnabled' % ctrlGrp, 1)
        
        # Use setAttr to assign color
        cmds.setAttr('%s.overrideColor' % ctrlGrp, colorVal)
        
        return ctrl

# Build upon the previous assignment, creating a
# functional FK control setup based on the following criteria:

# When selecting the root joint of a joint chain, create a control
# for it and all of it's descendant nodes (children, grandchildren, etc.)
# Parent and scale constrain each joint to it's respective control.
# Create an overall FK_Ctrl_Grp and parent all of the newly created
# FK control groups under this node.
# When a joint has multiple children, and branching occurs, create a
# control for that joint and then throw an error, indicating that the chain branches.

        
#----------------------------------
myCtrl = createControl('blue')