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
#create SQUARE control
def square(colorIndex):
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
            
            # Create Square:
            ctrl = cmds.curve(d=1, p=[(-1,0,1), (-1,0,-1), (1,0,-1), (1,0,1), (-1,0,1)], k=[0,1,2,3,4])
            
            #create group (parent -> control)
            ctrlShape = cmds.listRelatives(ctrl, shapes=True, children=True)[0]
            ctrlGrp = cmds.group(empty=True, name='square_%s_Grp' % ctrl)
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
        ctrl = cmds.curve(d=1, p=[(-1,0,1), (-1,0,-1), (1,0,-1), (1,0,1), (-1,0,1)], k=[0,1,2,3,4])
        
        #create group (parent -> control)
        ctrlShape = cmds.listRelatives(ctrl, shapes=True, children=True)[0]
        ctrlGrp = cmds.group(empty=True, name='square_%s_Grp' % ctrl)
        ctrl = cmds.parent(ctrl, ctrlGrp, a=True)[0]

        
        changeColor(colorIndex);
        
        # Find shape node  
        # Use setAttr to enable override
        cmds.setAttr('%s.overrideEnabled' % ctrlGrp, 1)
        
        # Use setAttr to assign color
        cmds.setAttr('%s.overrideColor' % ctrlGrp, colorVal)
        
        return ctrl
        
        
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

#----------------------------------
#create DIAMOND control
def diamond(colorIndex):
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
            
            # Create Diamond:
            ctrl = cmds.curve(d=1, p=[(-1,0,0), (0,0,-1), (1,0,0), (0,0,1), (-1,0,0)], k=[0,1,2,3,4])
            
            #create group (parent -> control)
            ctrlShape = cmds.listRelatives(ctrl, shapes=True, children=True)[0]
            ctrlGrp = cmds.group(empty=True, name='diamond_%s_Grp' % ctrl)
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
        ctrl = cmds.curve(d=1, p=[(-1,0,0), (0,0,-1), (1,0,0), (0,0,1), (-1,0,0)], k=[0,1,2,3,4])
        
        #create group (parent -> control)
        ctrlShape = cmds.listRelatives(ctrl, shapes=True, children=True)[0]
        ctrlGrp = cmds.group(empty=True, name='diamond_%s_Grp' % ctrl)
        ctrl = cmds.parent(ctrl, ctrlGrp, a=True)[0]

        
        changeColor(colorIndex);
        
        # Find shape node  
        # Use setAttr to enable override
        cmds.setAttr('%s.overrideEnabled' % ctrlGrp, 1)
        
        # Use setAttr to assign color
        cmds.setAttr('%s.overrideColor' % ctrlGrp, colorVal)
        
        return ctrl
        
        
#----------------------------------
#create STAR control
def star(colorIndex):
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
            
            # curve -d=1
            # -p=(-2, 0, 0)
            # -p=(-1.333333, 0, -1.155556)
            # -p=(0, 0, -3.466667)
            # -p=(2, 0, 1.866667)
            # -p=(-0.666667, 0, 1.955556)
            # -p=(-2, 0, 2)
            # -k 0 0 0 1 2 3 3 3 ;

            
            # Create Star:
            ctrl = cmds.curve(d=1, p=[(-2,0,0), (-1,0,-1), (0,0,-3), (2,0,2), (-1,0,2), (-2,0,2)], k=[0,1,2,3,4,6])
            
            #create group (parent -> control)
            ctrlShape = cmds.listRelatives(ctrl, shapes=True, children=True)[0]
            ctrlGrp = cmds.group(empty=True, name='diamond_%s_Grp' % ctrl)
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
        ctrl = cmds.curve(d=1, p=[(-2,0,0), (-1,0,-1), (0,0,-3), (2,0,2), (-1,0,2), (-2,0,2)], k=[0,1,2,3,4,6])
        
        #create group (parent -> control)
        ctrlShape = cmds.listRelatives(ctrl, shapes=True, children=True)[0]
        ctrlGrp = cmds.group(empty=True, name='diamond_%s_Grp' % ctrl)
        ctrl = cmds.parent(ctrl, ctrlGrp, a=True)[0]

        
        changeColor(colorIndex);
        
        # Find shape node  
        # Use setAttr to enable override
        cmds.setAttr('%s.overrideEnabled' % ctrlGrp, 1)
        
        # Use setAttr to assign color
        cmds.setAttr('%s.overrideColor' % ctrlGrp, colorVal)
        
        return ctrl    
        
#----------------------------------
myCtrl = square('blue')
myCtrl = circle('red')
myCtrl = diamond('purple')
#myCtrl = star('yellow')