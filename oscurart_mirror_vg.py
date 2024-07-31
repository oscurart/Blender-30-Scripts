#mirror vg from rigs _R to _L

import bpy
import bmesh


C = bpy.context
obj = bpy.context.object
bpy.context.scene.tool_settings.use_uv_select_sync = True
me = obj.data

#creates sym map
bm = bmesh.from_edit_mesh(me)
vertices = [vert.index for vert in bm.verts if vert.select]

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
            print(mirrorVert)
            try:
                i = group.weight(index)
            except:
                i = 0
            
            obj.vertex_groups[group.name.replace("_R","_L")].add([mirrorVert],i,"REPLACE")


