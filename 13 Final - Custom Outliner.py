import maya.cmds as cmds

print cmds.nodeType(sel)

#_______________________________________________________________________________
class Outliner():
    
    # INIT:
    def __init__(self):
        self.control_name = 'aaOutliner'
        self.node_types = ['joint', 'nurbsCurve', 'mesh', 'transform', 'clusterHandle', 'lattice', 'camera', 'parentConstraint', 'scaleConstraint']
    
    # CREATE:
    def create(self):
        self.delete()
        self.m_window = cmds.window(self.control_name)        
        self.m_column = cmds.columnLayout()
        
        sel = cmds.ls(sl=True)
        cmds.button(label='Find Nodes', command='FindNodeOfType(sel)')
        #self.m_row
        
        self.m_pane = cmds.paneLayout(parent=self.m_column, configuration='vertical2', staticWidthPane=1)
        self.node_list = cmds.textScrollList(parent=self.m_pane, append=self.node_types, allowMultiSelection=True)
        self.filter_list = cmds.textScrollList(parent=self.m_pane, allowMultiSelection=True, selectCommand=lambda *x: self.selectFilter(), doubleClickCommand=lambda *x: self.selectAll())
        cmds.showWindow(self.control_name)
        
    # DELETE:
    def delete(self):
        if cmds.window(self.control_name, exists=True):
            cmds.deleteUI(self.control_name)

    # EDIT LIST:
    def EditList(self):
        newNodes = ['aimConstraint', 'bend']
        self.node_types.extend()
        cmds.textScrollList(self.node_list, e=True, removeAll=True, append=self.node_types)

    # LIST FILTERED:
    def list_filtered(self):
        filter = cmds.textScrollList(self.node_list, query=True, selectItem=True)
        all_types = cmds.allNodeTypes()
        for f in filter[:]:
            if f not in all_types:
                filter.remove(f)
        
        if filter:
            nodes=[]  
            for type in filter:
                n = sorted(cmds.ls(type=type), key=lambda x: x.lower())
                
                if n and type in ['mesh', 'nurbsCurve', 'nurbsSurface', 'camera']:             
                    sorted(set(cmds.listRelatives(n, Parent=True)), key=lambda x: x.lower())
                
                nodes.extend(n)                
            cmds.textScrollList(self.filter_list, exists=True, removeAll=True, append=nodes)

    # SELECT FILTER:
    def selectFilter(self):
        selected = cmds.textScrollList(self.filter_list, query=True, selectItem=True)
        cmds.select(selected, replace=True)
        return
    
    # SELECT ALL
    def selectAll(self):
        selected = cmds.textScrollList(self.filter_list, query=True, allItems=True)
        cmds.textScrollList(self.filter_list, edit=True, selectItem=selected)
        self.select_filter()
        return
       
    # FIND NODE OF TYPE:
    def FindNodeOfType(node_Type):
        Print(node_Type)
        
        selectionList = []
        
        nodeType = 'mesh'
        filteredNodes = cmds.ls(types=node_Type)
        
        for item in filteredNodes:
            if cmds.node_Type() == 'mesh':
                i_xform = cmds.listRelatives(item, parent=True)
                selectionList.extend(i_xform)
            else:
                selectionList.append(item)
        
        cmds.select(selectionList, r=True)
        
        print(selectionList)
#_______________________________________________________________________________

myOutliner = Outliner()
myOutliner.create()