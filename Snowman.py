import maya.cmds as cmds

#Snowballs:
cmds.polySphere(subdivisionsX=20, subdivisionsY=20, radius=2.0)
cmds.polySphere(subdivisionsX=20, subdivisionsY=20, radius=1.5)
cmds.polySphere(subdivisionsX=20, subdivisionsY=20, radius=1.0)
cmds.move(0, 2.3, 0, 'pSphere2', relative=True)
cmds.move(0, 4.1, 0, 'pSphere3', relative=True)
cmds.rename('pSphere1', 'Base')
cmds.rename('pSphere2', 'Midsection')
cmds.rename('pSphere3', 'Head')

#Top Hat:
cmds.polyCylinder(subdivisionsX=20, subdivisionsY=1, subdivisionsZ=0, radius=1, height=0.2)
cmds.polyCylinder(subdivisionsX=20, subdivisionsY=1, subdivisionsZ=0, radius=0.7, height=1)
cmds.move(0, 0.5, 0, 'pCylinder2', relative=True)
cmds.polyUnite('pCylinder1', 'pCylinder2', ch=True, mergeUVSets=True, centerPivot=True)
cmds.delete('polySurface1', constructionHistory=True)
cmds.move(0, 4.8, 0, 'polySurface1', relative=True)
cmds.rename('polySurface1', 'Tophat')

#Nose:
cmds.polyCone(radius=1)
cmds.select('pCone1')
cmds.rotate(0.0, 0.0, '-90deg', relative=True)
cmds.move(1.5, 4.0, 0.0, 'pCone1', relative=True)
cmds.scale(0.1, 1.0, 0.1)
cmds.rename('pCone1', 'Nose')

#Eyes:
cmds.polyExtrudeFacet('Head.f[200]', 'Head.f[217]', keepFacesTogether=False, localTranslateZ=-0.2, localScale=(.5, .5, 0))

#Group All Objects Together:
cmds.group('Base', 'Midsection', 'Head', 'Tophat', 'Nose', name='Snowman')

#Move Entire Group Up:
cmds.move(0, 2, 0, 'Snowman', relative=True)

#Move Pivot Point:
cmds.move(0, -4, 0, 'Snowman.scalePivot', 'Snowman.rotatePivot', relative=True)

#Clear Selection:
cmds.select(clear=True)