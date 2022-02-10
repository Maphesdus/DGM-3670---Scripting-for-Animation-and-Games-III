import maya.cmds as cmds

# Create a list of the currently selected objects:
selectedObjects = cmds.ls(orderedSelection = True)

# Print the list:
print("Selected Objects (in order of selection): \n" + str(selectedObjects))

# Create an array to hold the joints:
jointList = []

# Create an index variable for working with the array:
index = 0

for obj in selectedObjects:
    # Replace the original selection list with its first object,
    # or replace the current object with the next list object:    
    cmds.select(obj, r=True)

    # Get the coordinates of the current object:
    x = cmds.getAttr("%s.translateX" % obj)
    y = cmds.getAttr("%s.translateY" % obj)
    z = cmds.getAttr("%s.translateZ" % obj)

    # Clear the selection so that the joint
    # doesn't get parented to the object:
    cmds.select(clear = True)
    
    # Create a joint at the center of the current object:
    jnt = cmds.joint(position=(x, y, z))
    jointList.append(jnt)
    
    # Parent the joint chain into a hierarchy matching the initial selection order.
    # Parent each joint under the previous joint:    
    if index >= 1:
        previousJnt = jointList[index-1]
        cmds.parent(jnt, previousJnt)
    else:
        previousJnt = None
    
    print("\nPrevious Joint: " + str(previousJnt))
    print("Current Joint: " + str(jnt))
    
    index += 1
    
print("\nJoint List: " + str(jointList))