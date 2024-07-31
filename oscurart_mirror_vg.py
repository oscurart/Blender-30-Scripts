#mirror vg one side to another
#select in edit mode

import bpy
import bmesh


C = bpy.context
obj = bpy.context.object
me = obj.data

#creates sym map
bpy.ops.object.mode_set(mode="EDIT")
bm = bmesh.from_edit_mesh(me)
vertices = [vert.index for vert in bm.verts if vert.select]
vg = bpy.context.object.vertex_groups.active
mirDict = {} 

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
        i = vg.weight(index)
    except:
        i = 0     
               
    mirDict[mirrorVert] = i


for index,value in mirDict.items():
    print(index)
    print(value)
    vg.add([index], value,"REPLACE")

bpy.ops.object.mode_set(mode="WEIGHT_PAINT") 
