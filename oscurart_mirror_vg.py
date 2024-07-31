#mirror vg from rigs _R to _L

import bpy
import bmesh


C = bpy.context
obj = bpy.context.object
me = obj.data

#creates sym map
bpy.ops.object.mode_set(mode="EDIT")
bm = bmesh.from_edit_mesh(me)
vertices = [vert.index for vert in bm.verts]
mirDict = {} 
for group in obj.vertex_groups:
    if group.name.count("_R"):
        for index in vertices:            
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_all(action="DESELECT")  
            bpy.ops.object.mode_set(mode="OBJECT")  
            me.vertices[index].select = True
            bpy.ops.object.mode_set(mode="EDIT")
            bpy.ops.mesh.select_mirror()
            bpy.ops.object.mode_set(mode="OBJECT") 
            mirrorVert = [mirrorvert.index for mirrorvert in me.vertices if mirrorvert.select][0]
            try:
                i = group.weight(index)
            except:
                i = 0            
            mirDict[mirrorVert] = [i, group.name.replace("_R","_L")]
            #obj.vertex_groups[group.name.replace("_R","_L")].add([mirrorVert],i,"REPLACE")


for index,value in mirDict.items():
    obj.vertex_groups[value[1]].add([index], value[0],"REPLACE")
