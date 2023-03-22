import bpy
from mathutils import Vector
 
 
me = bpy.context.active_object.data 
me.calc_tangents(uvmap = bpy.context.object.data.uv_layers.active.name)

for face in me.polygons:
    # face loops and face vertices are in the same order
    for vert_id, loop_id in zip(face.vertices, face.loop_indices):    
        # this is the loop:
        me.loops[loop_id]
        # this is the vertex in the corner of the loop:
        #me.vertices[vert_id]
        print(me.loops[loop_id].index)
        me.attributes.active.data[vert_id].vector = me.loops[me.loops[loop_id].index].tangent 